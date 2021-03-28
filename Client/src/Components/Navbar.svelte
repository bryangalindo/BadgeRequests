<script>
    let src = "./images/navbar_logo.jpg";
</script>

<nav>
    <div class="flex">
        <a href="/"><img {src}></a>
    </div>
</nav>


<style>
    nav {
      background-color: #fff;
      height: 70px;
      box-shadow: 0 3px 3px 0 rgba(0, 0, 0, 0.2);
    }

    .flex {
        display: flex;
    }

    img {
        margin-top: 16px;
        padding-left: 50px;
        padding-right: 20px;
    }
  
  </style>