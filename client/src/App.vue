<template>
  <router-view/>
</template>

<script>
import Registration from '@/components/Registration.vue'
import Authentication from '@/components/Authentication.vue'


export default {
  name: 'HomeView',
  components: {
    Registration,
    Authentication
  }
}
</script>

<style>
  html{
    box-sizing: border-box;
    background-color: #F5F5F5;
  }

  *,
  *::after,
  *::before{
    box-sizing: inherit;
  }

  ul[class],
  ol[class] {
    padding: 0;
  }

  body,
  h1,
  h2,
  h3,
  h4,
  h5,
  h6,
  p,
  ul,
  ol,
  li,
  figure,
  figcaption,
  blockquote,
  dl,
  dd {
    margin: 0;
  }

  ul[class] {
    list-style: none;
  }

  img {
    max-width: 100%;
    display: block;
  }

  input,
  button,
  textarea,
  select {
    font: inherit;
  }

  a{
    text-decoration: none;
  }
</style>
