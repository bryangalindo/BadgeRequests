<script lang="ts">
    import { onMount } from 'svelte';
    import axios from 'axios';

    import Navbar from './Components/Navbar.svelte';
    import Card from './Components/Card.svelte';
    import Sidebar from './Components/Sidebar.svelte';

    let authData = { email: '', name: '', avatar: ''};
    let src = "./images/btn_google_signin.png";

    onMount(() => {
        const getRequest = axios
            .get(`http://localhost:8000/api/v1/auth/me`, { withCredentials: true })
            .then((res) => {
                authData = res.data;
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


<div class="container">
    {#if !authData.email}
        <a class="login" href="http://localhost:8000/login"><img class="centered" src={src} alt="Login Button" /></a>
    {:else}
        <div class="header">
            <Navbar name={authData.name} avatar={authData.avatar}/>
        </div>
        <div class="body">
            {#await promise}
                <div class="spinner">Loading...</div>
            {:then data}
                <div class="sidebar">
                    <Sidebar email={authData.email}/>
                </div>
                <div class="content">
                    {#each Object.entries(data) as [category, badges]}
                        <h1><span><em>{category}</em></span></h1>
                        <div class="cards">
                            {#each badges as badge}
                                <Card id={badge.RowKey} description={badge.Description} title={badge.Title} exp={badge.Exp}/>
                            {/each}
                        </div>
                    {/each}
                </div>
            {:catch error}
                <div class="uppercase text-red-700">{error.message}</div>
            {/await}
        </div>
    {/if}
</div>

<style>
	h1 {
        font-family: 'Press Start 2P', cursive;
		color: #343A40;
		text-transform: uppercase;
		font-size: 3.5em;
		word-spacing: -15px;
        text-align: left;
        margin-top: 10px;
        margin-left: 10px;
        margin-bottom: 15px;
	}

    h1 span {
        background: linear-gradient(180deg, rgba(255,255,255,0) 75%, rgb(240,210,78) 80%);
    }

    .cards {
        display: flex;
        flex-wrap: wrap;
    }

    .centered {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }

    .content {
        overflow-y: scroll;
        padding: 20px;
        margin-left: 40px;
    }

    .header {
        background-color: #343A40;
    }

    img.centered {
        max-width: 225px;
        max-height: 150px;
    }

    .sidebar {
        border-right: solid 1px lightgrey;
        position: relative;
    }

    /* Extra small devices (phones, 600px and down) */
    @media only screen and (max-width: 600px) {
        h1 {
            text-transform: uppercase;
            font-size: 3em;
            font-weight: bold;
	    }

        .body {
            display: grid;
            grid-template-columns: 1fr;
            overflow: hidden;
        }

        .content {
            margin-left: 10px;
            order: 1;
        }

        .sidebar {
            order: 2;
        }
    }
</style>
