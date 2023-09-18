<template>
    <span v-if="status_token === true">
        <header header__home>
            <div class="container">
                <div class="menu_home">
                    <div class="logo_home">
                        <a href="" class="logo">
                            <img src="../img/logo_page1.png" @click="exit_profile">
                        </a>
                        <div class="logo__desc">UMOM ПОИСК</div>
                    </div>
                    <a href="#home" class="menu__home__link">Поиск</a>
                    <a href="#news" class="menu__home__link">История</a>
                    <div class="dropdown">
                        <button class="dropbtn">{{ login_user }}
                            <i class="fa fa-caret-down"></i>
                        </button>
                        <div class="dropdown-content">
                            <router-link to="/profile">Профиль</router-link>
                            <a @click="exit_profile">Выход</a>
                        </div>
                    </div>
                </div>
            </div>
        </header>
        <section v-if="status_search" class="search">
            <div class="container">
                <div class="block__search">
                    <div class="seacrch__txt">Поиск команды</div>
                    <div class="info">
                        <div class="search_work">
                            <p class="search_work_p">Ваша специальность</p>
                            <p class="search_work_answer">{{ value_speciality }}</p>
                        </div>
                        <div class="search__stack">
                            <p class="search_stack_p">Ваш стэк</p>
                            <p class="search_stack_answer">{{ value_stack }}</p>
                        </div>
                    </div>
                    <div class="run__search__team">Идет поиск команды</div>
                    <div class="spin-wrapper">
                        <div class="spinner">
                        </div>
                        <button v-if="start_search" @click="search_team" class="search__btn">Начать поиск</button>
                        <button v-else @click="stop_search" class="search__btn__false">Остановить</button>
                    </div>
                    <div class="info_error" v-if="error_msg">Чтобы искать команду необходимо заполнить профиль </div>
                </div>
            </div>
        </section>
        <section v-else class="search">
            <div class="container">
                <div class="block__search">
                    <div class="seacrch__txt">Команда найдена</div>
                    <p>Ваша команда</p>
                    <div v-for="(item, index) in user_info" class="people">
                        <div class="login">Login:
                            <div>{{ item.login }}</div>
                        </div>
                        <div class="contact">contacts:
                            <div>discord: {{ item.discord }}</div>
                            <div>telegram: {{ item.telegram }}</div>
                        </div>
                        <div class="steck">Stack:
                            <div> {{ item.stack }} </div>
                        </div>
                        <div class="special">Speciality:
                            <div> {{ item.job_title }}</div>
                        </div>
                    </div>
                    <div class="people_btn">
                        <button class="crash__team" @click="delete_team">Расформировать состав</button>
                        <div class="modal_crash_team" id="modal_crash_team" v-if="team_status">
                            <div class="">
                                <h2>Голосование за расформирование</h2>
                                <p class="modal__txt">3 / 4</p>
                                <div class="modal__btn">
                                    <button class="close" @click="leave_in_the_team">Расформировать</button>
                                    <button class="open" @click="leave_in_the_team">Покинуть</button>
                                </div>
                            </div>
                            <a href="#close" class="css-modal-close"></a>
                        </div>
                        <button class="join__team" @click="leave_team">Покинуть команду</button>
                        <div class="modal_join_team" id="modal_join_team" v-if="leave_team_status">
                            <div class="">
                                <h2>Вы уверены что хотите покинуть команду?</h2>
                                <p class="modal__txt">Если вы покинете команду, вы будете отстранены от поиска на 24 часа.</p>
                                <div class="modal__btn">
                                    <button class="close" @click="leave_in_the_team">Остаться</button>
                                    <button class="open" @click="leave_in_the_team">Покинуть</button>
                                </div>
                            </div>
                            <a href="#close" class="css-modal-close"></a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </span>
  </template>

<script>
import axios from 'axios';

export default {
    name: 'MainPage',
    data(){
        return{
            login_user: '',
            status_token:false,
            value_speciality: '        ',
            value_stack:'        ',
            error_msg: '',
            timeId: '',
            start_search: true,
            status_search: true,
            user_info: '',
            team_status: false,
            leave_team_status: false
        }
    },
    async created(){
        await axios.post('http://127.0.0.1:8000/home', {
          token:localStorage.getItem('token'),
        })
        .then((response) => {
            if (response.status == 200){
                this.status_token = true
                console.log("token ok")
                this.login_user = localStorage.getItem('login')
                this.get_user_info()
            }
        })
        .catch((error) => {
            this.$router.push('/auth')
            console.log(error);
        });
    },
    methods:{
        exit_profile(){
            axios.post('http://127.0.0.1:8000/logout', {
                token:localStorage.getItem('token'),
            })
            .then((response) => {
                if (response.status == 200){
                    this.$router.push('/auth')
                    clearInterval(this.timeId)
                }
            })
            .catch(function (error) {
                console.log(error);
            })
        },
        get_user_info(){
            axios.post('http://127.0.0.1:8000/getprofile', {
                token:localStorage.getItem('token'),
            })
            .then((response) => {
                if (response.data.message == "None"){
                    this.error_msg = "Чтобы искать команду необходимо заполнить профиль"
                } else {
                    this.value_speciality = response.data.job_title,
                    this.value_stack = response.data.stack
                }
            })
            .catch((error) => {
                console.log(error)
            });
        },
        search_team(){
            axios.post('http://127.0.0.1:8000/getteam', {
                token:localStorage.getItem('token'),
            })
            .then((response) => {
                this.start_search = false
                this.timeId = setInterval(() =>
                    this.check_Teammate(response)
                ,5000)
            })
            .catch((error) => {
                console.log(error)
            });
        },
        check_Teammate(response){
            if (response.data[0] && response.data[1] && response.data[2] && response.data[3]){
                this.status_search = false
                clearInterval(this.timeId)
                this.user_info = response.data
                console.log(this.user_info)
            } else {
                console.log(response.data)
                console.log("wait")
            }
        },
        stop_search(){
            clearInterval(this.timeId)
            this.start_search = true
        },
        delete_team(){
            this.team_status = true
        },
        leave_in_the_team(){
            this.team_status = false
            this.status_search = true
        },
        leave_team(){
            this.leave_team_status = true
        }
    }
}
</script>

<style>

@import '@/style/style.css';

</style>