<template>
    <header header__home>
        <div class="container">
            <div class="menu_home">
                <div class="logo_home">
                    <a href="" class="logo">
                        <!-- <img src="../img/logo_page1.png" alt=""> -->
                    </a>
                    <div class="logo__desc">UMOM ПОИСК</div>
                </div>
                <a @click="go_to_home" class="menu__home__link">Поиск</a>
                <a href="#news" class="menu__home__link">История</a>
                <div class="dropdown">
                    <button class="dropbtn">{{ login }}
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
    <section class="section__profile">
        <p v-if="errors.length">
            <b>Пожалуйста исправьте указанные ошибки:</b>
        <ul>
            <li v-for="error in errors">{{ error }}</li>
        </ul>
        </p>
        <div class="container">
            <div class="profile__block">
                <div class="block__img">
                    <!-- <div class="profile__img"><img src="../img/logo_page1.png" alt=""></div> -->
                    <div class="profile__oflain">Online</div>
                    <div class="profile__status">
                        <p>Cтатус</p>
                        <!-- <a href=""><img src="../img/pen.svg" alt=""></a> -->
                    </div>
                </div>
                <div class="elem__profile">
                    <div class="name">
                        <h2 class="name__user">Имя Фамилия</h2>
                        <p class="name__status">{{ login }}</p>
                    </div>
                    <div class="about__me">
                        <form action="">
                            <p class="about__me__txt"> О себе</p>>
                            <p><textarea name="comment" cols="40" rows="3"
                                    v-model="description"></textarea></p>
                            <p class="about__me__btn"><input value="Сохранить"></p>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <section class="anketa">
        <div class="container">
            <h2 class="anketa__title">Персональная анкета</h2>
            <div class="anketa__block">
                <div class="anketa_label">
                    <label class="anketa_specialist">Специальность<sup>*</sup>
                    </label>
                    <select id="selectvalue" class="anketa_specialis_sel"
                        v-model="value_speciality"
                        @click="output_console_value(value_speciality)">
                        <option v-for="(item, index) in dict_speciality">
                            {{ item.ru }}
                        </option>
                    </select>
                </div>
                <div class="anketa_label">
                    <label class="anketa_stack">Стэк<sup>*</sup> </label>
                    <select id="selectvalue" class="anketa_stack_sel"
                        v-model="value_stack"
                        @click="output_console_value(value_stack)">
                        <option
                            v-if="value_speciality === dict_speciality.front.ru"
                            v-for="(item, index) in dict_stack.front">
                            {{ item }}
                        </option>
                        <option
                            v-else-if="value_speciality === dict_speciality.back.ru"
                            v-for="(item, index) in dict_stack.back">
                            {{ item }}
                        </option>
                        <option
                            v-else-if="value_speciality === dict_speciality.design.ru"
                            v-for="(item, index) in dict_stack.design">
                            {{ item }}
                        </option>
                        <option
                            v-else-if="value_speciality === dict_speciality.layout.ru"
                            v-for="(item, index) in dict_stack.layout">
                            {{ item }}
                        </option>
                    </select>
                </div>
                <div class="anketa_label">
                    <label class="anketa_pract">Опыт<sup>*</sup> </label><select
                        id="selectvalue" class="anketa_pract_sel"
                        v-model="value_experience"
                        @click="output_console_value(value_experience)">
                        <option v-for="(item, index) in dict_experience">
                            {{ item }}
                        </option>
                    </select>
                </div>
                <p class="about__me__btn"><input type="submit" value="Сохранить">
                </p>
            </div>
            <p class="anketa__desc"><sup>*</sup> Обязательно для заполнения</p>
        </div>
    </section>
    <section class="connect_profile">
        <div class="container">
            <h3 class="connect_title">Контакты</h3>
            <p class="connect__desc">Для связи с будущими тиммейтами необходимо
                указать контакты, по которым можно будет с вами связаться.</p>
            <div class="connect__block">
                <label>Telegram<sup>*</sup> <input type="text"
                        v-model="telegram" /></label>
                <label class="discord_profile">Discord <sup>*</sup> <input
                        type="text" v-model="discord" /></label>
                <p class="about__me__btn"><input @click="post" value="Сохранить">
                </p>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Profile',
    data() {
        return {
            dict_speciality: {
                front: {
                    ru: "Фронтэнд",
                    us: "frontend"
                },
                back: {
                    ru: "Бекэнд",
                    us: "backend"
                },
                design: {
                    ru: "Дизайн",
                    us: "design"
                },
                layout: {
                    ru: "Верстальщик",
                    us: "typesetter"
                }
            },
            dict_stack: {
                front: {
                    1: 'Vue',
                    2: 'Angular',
                    3: 'React',
                    4: 'JS'
                },
                back: {
                    1: 'Python FastAPI',
                    2: 'Node JS',
                    3: 'PHP'
                },
                design: {
                    1: 'Figma',
                    2: 'xz chto tam est eche'
                },
                layout: {
                    1: 'html',
                    2: 'sass/scss'
                }
            },
            dict_experience: {
                1: '1 год',
                2: 'более двух лет',
                3: 'более пяти лет',
            },
            value_speciality: '',
            value_stack: '',
            value_experience: '',
            telegram: '',
            discord: '',
            description: '',
            status: 'Online',
            errors: [],
            login: ''
        }
    },
    async created() {
        await axios.post('http://127.0.0.1:8000/getprofile', {
            token: localStorage.getItem('token'),
        })
            .then((response) => {
                this.login = localStorage.getItem('login')
                if (response.data.message == "None") {
                    console.log("not profile")
                } else {
                    this.value_experience = response.data.experience,
                        this.description = response.data.description,
                        this.discord = response.data.discord,
                        this.value_speciality = response.data.job_title,
                        this.value_stack = response.data.stack,
                        this.status = response.data.status,
                        this.telegram = response.data.telegram
                }
            })
            .catch((error) => {
                // console.log(error)
            });
    },
    methods: {
        check() {
            this.checkForm()
            // console.log(
            //     "token:", localStorage.getItem('token'),
            //     "\nlogin:", localStorage.getItem('login'),
            //     "\nstatus:", this.status,
            //     "\njob_title:", this.check_value_speciality(),
            //     "\nstack:", this.value_stack,
            //     "\nexperience:", this.value_experience,
            //     "\ndescription:", this.description,
            //     "\ntelegram:", this.telegram,
            //     "\ndiscord:", this.discord
            // )
        },
        post() {
            axios.post('http://127.0.0.1:8000/profile', {
                token: localStorage.getItem('token'),
                login: localStorage.getItem('login'),
                status: this.status,
                job_title: this.check_value_speciality(),
                stack: this.value_stack,
                experience: this.value_experience,
                description: this.description,
                telegram: this.telegram,
                discord: this.discord
            })
                .then((response) => {
                    if (response.status == 200) {
                        // console.log("ok")
                    }
                })
                .catch(function (error) {
                    // console.log(error);
                });
        },
        output_console_value(value) {
            // console.log(value)
        },
        checkForm() {
            if (this.description && this.value_speciality && this.value_stack && this.value_experience && this.telegram && this.discord) {
                return true
            }
            this.errors = []
            if (!this.description) {
                this.errors.push('Требуется указать "О себе"')
            }
            if (!this.value_speciality) {
                this.errors.push('Требуется указать "Специальность"')
            }
            if (!this.value_stack) {
                this.errors.push('Требуется указать "Стэк"')
            }
            if (!this.value_experience) {
                this.errors.push('Требуется указать "Опыт"')
            }
            if (!this.telegram) {
                this.errors.push('Требуется указать "telegram"')
            }
            if (!this.discord) {
                this.errors.push('Требуется указать "discord"')
            }
        },
        go_to_home() {
            this.$router.push('/main')
        },
        check_value_speciality() {
            if (this.value_speciality === "Фронтэнд") {
                return this.dict_speciality.front.us
            }
            if (this.value_speciality === "Верстальщик") {
                return this.dict_speciality.layout.us
            }
            if (this.value_speciality === "Дизайн") {
                return this.dict_speciality.design.us
            }
            if (this.value_speciality === "Бекэнд") {
                return this.dict_speciality.back.us
            }
        },
        exit_profile() {
            axios.post('http://127.0.0.1:8000/logout', {
                token: localStorage.getItem('token'),
            })
                .then((response) => {
                    if (response.status == 200) {
                        this.$router.push('/auth')
                        clearInterval(this.timeId)
                    }
                })
                .catch(function (error) {
                    // console.log(error);
                })
        }
    }
}
</script>
