
<template>
    <div class="card">
        <slot></slot>
        <aside class="back">
            <a class="tlp-zoom" href="https://tecnovedadesweb.com/wp-content/uploads/2022/10/TwentyDivine.png" aria-label="Twenty Divine"><i class="fa-solid fa-magnifying-glass-plus"></i></a>
            <a href="https://tecnovedadesweb.com/portfolio/twenty-divine/" aria-label="Twenty Divine"><i class="fa-solid fa-up-right-from-square"></i></a>
        </aside>
    </div></template>
<style scoped>
.card{
    transition: all 200ms linear;
}
.card:hover{
    .back{
        opacity: 1;        
    }
}
.back{
    opacity: 0;
    z-index: 10;    
    position: absolute;
    inset: 0px;
    background-color: var(--fg-color-3);    
    transition: all 200ms linear;
    display: flex;
    justify-content: center;
    gap: 1em;
    a{
        border-radius: 50%;
        padding: 15px;
        color: var(--fg-color-1);
        border: solid 1px var(--fg-color-1);
        i{
            color: inherit;
        }
    }
}
</style>
<script lang="ts">

</script>