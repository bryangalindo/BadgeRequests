<script>
    import BadgeStore from '../Stores/BadgeStore.js';

    export let title;
    export let description;
    export let id;
    export let exp;

    let badgesToSubmit = [];

    const handleClick = (id, title, exp) => {
    const currentIndex = badgesToSubmit.indexOf(id);
    const badgeObject = {"id": id, "title": title, "exp": exp};
    const button = document.getElementById("button");

    if (currentIndex === -1) {
        badgesToSubmit.push(id);
        badgesToSubmit = badgesToSubmit;
        BadgeStore.update(currentBadges => {
        return [...currentBadges, badgeObject]
    })
    } else {
        badgesToSubmit.splice(currentIndex, 1);
        badgesToSubmit = badgesToSubmit;
        $BadgeStore = $BadgeStore.filter(badge => {
            return badge.id !== id
        })
        $BadgeStore = $BadgeStore;
    }

    if ($BadgeStore.length === 0) {
            button.disabled = true
        } else {
            button.disabled = false
        }

  }
</script>

<div class="card">
    <h3>{title}</h3>
    <p>{description}</p>
    <input on:click={() => handleClick(id, title, exp)} type="checkbox" id="{id}" name="badge_id" value="{id}">
</div>

<style>
    h3 {
        margin: 2px 5px;
        text-align: left;
        background: linear-gradient(180deg, rgba(255,255,255,0) 85%, rgb(48, 204, 183) 80%);
    }

    p {
        margin: 2px 5px;
        text-align: left;
        font-size: small;
    }

    .card {
        box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);
        padding-top: 16px;
        padding-left: 16px;
        padding-right: 16px;
        text-align: right;
        background-color: #ffff;
        border-radius: 4px;
        flex-basis: 20%;
        margin: 5px 5px;
    }
    /* Extra small devices (phones, 600px and down) */
    @media only screen and (max-width: 600px) {
        .card {
            flex-basis: 82%;
        }
    }

    /* Small devices (portrait tablets and large phones, 600px and up) */
    @media only screen and (min-width: 600px) {
        .card {
            flex-basis: 100%;
        }
    }

    /* Medium devices (landscape tablets, 768px and up) */
    @media only screen and (min-width: 768px) {
        .card {
            flex-basis: 100%;
        }
    }

    /* Large devices (laptops/desktops, 992px and up) */
    @media only screen and (min-width: 992px) {
        .card {
            flex-basis: 40%;
        }
    }

    /* Extra large devices (large laptops and desktops, 1200px and up) */
    @media only screen and (min-width: 1500px) {
        .card {
            flex-basis: 25%;
        }
    }

    /* Extra large devices (large laptops and desktops, 1600px and up) */
    @media only screen and (min-width: 1750px) {
        .card {
            flex-basis: 20%;
        }
    }

</style>