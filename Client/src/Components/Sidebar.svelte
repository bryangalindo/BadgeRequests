<script>
    import BadgeStore from '../Stores/BadgeStore.js';
    import { v4 as uuidv4 } from 'uuid';

    export let email;

    const prepareBadgeArray = (badges, email, id) => {
        const preparedBadgeArray = [];

        for (const badge of badges) {
            const badgeRowKey = uuidv4();
            badge['PartitionKey'] = email;
            badge['RowKey'] = badgeRowKey;
            badge['ApplicationID'] = id;
            badge['approved'] = false;
            badge['approved_by'] = "";
            badge['badgeID'] = badge.id;
            delete badge['exp'];
            delete badge['id'];
            preparedBadgeArray.push(badge);
        }
        return preparedBadgeArray;
    }

    const prepareApplicationObject = (badges, email, id) => {
        const preparedBadges = prepareBadgeArray(badges, email, id);
        const applicationObject = {
            'PartitionKey': email,
            'RowKey': id,
            'requests': preparedBadges,
        }

        return applicationObject;
    }

    const sendGoogleChatNotification = async (application) => {
        const response = await fetch("http://localhost:8000/notify", {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(application),
            credentials: 'include'
        });
        const data = await response.json();
        console.log(data);
        if (response.ok) {
            return console.log("Successfully notified Google Chat");
        } else {
            throw new Error(data);
        }
    }
    
    const handleSubmit = async () => {
        const id = uuidv4();
        const applicationObject = prepareApplicationObject($BadgeStore, email, id);
        sendGoogleChatNotification(applicationObject)
        const response = await fetch("http://localhost:8000/api/v1/applications/", {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(applicationObject),
            credentials: 'include'
        });
        const data = await response.json();
        if (response.ok) {
            alert('SUCCESS! Your badge application was successfully submitted.')
            window.location.replace("http://localhost:5000/");
        } else {
            alert('UH OH! We did not receive your application. Try again.')
            window.location.replace("http://localhost:5000/");
            throw new Error(data);
        }
    }
</script>

<h1><span>Badge Cart</span></h1>
{#if $BadgeStore}
    {#each $BadgeStore as badge}
        <ul>
            <li>{badge.title} <b>[EXP: {badge.exp}]</b></li>
        </ul>
    {/each}
    <div class="wrapper">
        <input type="submit" on:click={() => handleSubmit()} class="button fixed block" value="Submit">
    </div>
{/if}

<style>
    h1 {
        margin-top: 20px;
        margin-bottom: 20px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        text-align: center;
        font-weight: 600;
    }

    h1 span {
        background: linear-gradient(180deg, rgba(255,255,255,0) 80%, rgb(48, 204, 183) 80%);
    }

    li {
        margin: 10px auto;
        list-style: none;
        font-size: small;
        text-align: center;

    }

    .button {
        font-family: 'Roboto', sans-serif;
        background-color: rgb(234, 67, 77) ;
        color: white;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-radius: 5px;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        transition-duration: 0.4s;
    }

    .button:hover {
        color: white;
    }

    .block {
        display: inline-block;
        width: 75%; 
        border: none;
        padding: 14px 28px;
        font-size: 16px;
        cursor: pointer;
        position: absolute;
        bottom: 0px;
    }

    .wrapper {
        display: flex;
        justify-content: center;
    }

    /* Extra small devices (phones, 600px and down) */
    @media only screen and (max-width: 600px) {
        ul {
            display: none;
            visibility: none;
        }

        .block {
            width: 75%; 
            padding: 5px 10px;
        }
}
</style>