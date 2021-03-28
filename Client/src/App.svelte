<script lang="ts">
    import { onMount } from 'svelte';
    import axios from 'axios';

    import Navbar from './Components/Navbar.svelte';
    import Card from './Components/Card.svelte';
    import Sidebar from './Components/Sidebar.svelte';

    let data = { email: '', name: '' };
    let src = "./images/btn_google_signin.png";

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
    
    const groupBy = (_array, key) => {
        return _array.reduce(
                function(rv, x) {
                    (rv[x[key]] = rv[x[key]] || []).push(x);
                    return rv;
                }, 
            {});
    };

	async function getBackendData() {
		const response = await fetch("http://localhost:8000/api/v1/badges/", {
            credentials: 'include'
        });
		const data = await response.json();
		if (response.ok) {
            const badgesGroupedByCategory = groupBy(data, 'PartitionKey');
            return badgesGroupedByCategory;
		} else {
			throw new Error(data);
		}
	}

	let promise = getBackendData();
</script>

  {#if !data.email}
    <a class="login" href="http://localhost:8000/login"><img class="centered" src={src} alt="Login Button" /></a>
  {:else}
  <Navbar />
  <main>
    <Sidebar email={data.email}/>
    <p>Welcome {data.name}!</p>
    <a class="logout" href="http://localhost:8000/logout">LOGOUT</a>
    {#await promise}
	    <div class="spinner">Spinner Here</div>
	{:then data}
    {#each Object.entries(data) as [category, badges]}
        <div>
            <h1>{category}</h1>
        </div>  
        <div class="container">
            <div class="row">
                {#each badges as badge}
                    <Card id={badge.RowKey} description={badge.Description} title={badge.Title} exp={badge.Exp}/>
                {/each}
            </div>
        </div>
    {/each}
	{:catch error}
		<div class="uppercase text-red-700">{error.message}</div>
	{/await}
    </main>
  {/if}



<style>
    main {
        text-align: center;
        padding: 1em;
        max-width: 240px;
        margin: 0 auto;
    }

	h1 {
		color: #595959;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
        text-align: left;
        padding-left: 275px;
	}

    img {
        max-width: 225px;
        max-height: 150px;
    }

    .centered {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }


    @media (min-width: 640px) {
        main {
            max-width: none;
        }
    }
</style>
