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
        console.log(data);
        if (response.ok) {
            return console.log("Success");
        } else {
            throw new Error(data);
        }
    }
</script>

<nav>
    <h2>Selected Badges</h2>
    {#if $BadgeStore}
    {#each $BadgeStore as badge}
        <ul>
            <li>{badge.title} <b>[EXP: {badge.exp}]</b></li>
        </ul>
    {/each}
    <input type="submit" on:click={() => handleSubmit()} class="fixedButton" value="Submit">
    {/if}
</nav>


<style>
    nav {
        position: fixed;
        top: 0;
        right: 0;
        height: 100%;
        padding: 2rem 1rem 0.6rem;
        border-left: 1px solid #aaa;
        background: #fff;
        width: 20rem;
    }

    .fixedButton{
            position: fixed;
            bottom: 0px;
            right: 110px; 
            margin: flex;
            padding: 20px;
        }
</style>