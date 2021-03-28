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

  }
</script>

<div class="column">
    <div class="card">
        <h3>{title}</h3>
        <p>{description}</p>
        <input on:click={() => handleClick(id, title, exp)} type="checkbox" id="{id}" name="badge_id" value="{id}">
    </div>
</div>

<style>
    .card {
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    padding-top: 16px;
    padding-left: 16px;
    padding-right: 16px;
    text-align: center;
    background-color: #ffff;
    border-radius: 12.5px;
    }

    input {
        margin-top: 8px;
        margin-bottom: 15px;
        text-align: right;
    }
</style>