<script>
    let src = "./images/navbar_logo.jpg";
    export let name;
    export let avatar;
</script>

<div class="flexbox">
    <ul>
        <li><a href="/"><img class="logo"{src} alt="logo"></a></li>
        <li><h1>HCSS Badge Shop</h1>
        </li>
    </ul>
    <ul>
        <li><p>Welcome, <b>{name}</b>!</p></li>
        <li><img class="avatar wrap" src={avatar} alt="avatar"/></li>
    </ul>
</div>

<style>
    h1 {
        font-family: 'Press Start 2P', cursive;
        word-spacing: -15px;
        margin-top: 12px;
        margin-left: -10px;
        color:white;
        text-transform: uppercase;
        letter-spacing: 1.25px;
        font-size: large;
    }

    p {
        margin-top: 12px;
        color:white;
    }

    ul {        
        display: flex;
        align-items: center;
    }

    ul li {
        margin-right: 20px;
    }

    .flexbox {
        display: flex;
        justify-content:space-between;
        align-items: center;
        align-self: center;
    }

    img.avatar {
        width: 50px;
        height: 50px;
        background-size: cover;
        background-position: top center;
        border-radius: 50%;
        margin-top: 15px; 
        margin-right: 30px
    }

    img.logo {
        margin-top: 15px;
        padding-left: 50px;
        padding-right: 20px;
    }


    /* Mobile devices (phones, 600px and down) */
    @media only screen and (max-width: 600px) {
        h1 {
            visibility: hidden;
            display: none
        }

        img.avatar {
            width: 50px;
            height: 50px;
            background-size: cover;
            background-position: top center;
            border-radius: 50%;
            margin-top: 15px; 
            margin-right: 10px
        }

        img.logo {
            margin-top: 15px;
            margin-left: 15px;
            padding: 5px;
        }
    }
  </style>