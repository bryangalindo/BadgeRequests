<script lang="ts">
  import { onMount } from 'svelte';
  import axios from 'axios';
  export let name: string;
  let data = { email: '', name: '' };
  onMount(() => {
    const getRequest = axios
      .get(`http://localhost:8000/api/v1/auth/me`, { withCredentials: true })
      .then((res) => {
        data = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  });
</script>

<main>
  <h1>Hello {name}!</h1>
  <p>
    Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn
    how to build Svelte apps.
  </p>
  {#if !data.email}
    <a class="login" href="http://localhost:8000/login">LOGIN</a>
  {:else}
    <p>Welcome {data.name}!</p>
    <a class="logout" href="http://localhost:8000/logout">LOGOUT</a>
  {/if}
</main>

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>
