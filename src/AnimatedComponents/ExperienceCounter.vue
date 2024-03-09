<template>
     <div class="experience" id="container">
        <h1><span> + {{ counter }}</span> <br/>Años en el mercado</h1>
        <svg
          class="elipse"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 1000 100"
          preserveAspectRatio="none"
        >
          <path
            class="elementor-shape-fill"
            d="M500,97C126.7,96.3,0.8,19.8,0,0v100l1000,0V1C1000,19.4,873.3,97.8,500,97z"
          ></path>
        </svg>
      </div>
</template>
<script setup lang="ts">
import Scrollbar from 'smooth-scrollbar';
import {ref} from 'vue'
const counter = ref(0)
const blocking = ref(false)
const scroll =  Scrollbar.get(document.getElementById("my-scrollbar")!)
const $container = document.getElementById('container')

const elementInView = ( percentageScroll = 100) => {               
    return (        
     scroll?.isVisible(document.getElementById("container")!)
    );
};
const incrementCounterAsync = () =>{
    console.log(blocking.value);
    
    return new Promise<void>((resolve, reject) => {
      setTimeout(()=>{        
        counter.value++;
      },1000)  
    })
}
scroll?.addListener(()=>{
    if(elementInView() && !blocking.value){
        blocking.value=true     
      // Asegúrate de que el contador no se reinicie si ya está en marcha
        if (counter.value === 0) {
            const interval = setInterval(() => {
                counter.value++;
            // Puedes ajustar la duración y el valor final según tus necesidades
                if (counter.value === 10) {
                    clearInterval(interval);
                }
            }, 1000);
        } 
        blocking.value=false
    }
    
})
</script>
<style scoped>
 .elipse {
    height: 240px;
    width: 100%;
    position: absolute;
    top: 0;
    bottom: 0;
    transform: rotate(180deg);
    path {
      fill: #ffffff;
    }
  }
  .experience {
    position: relative;
    height: 150px;
    overflow-y: hidden;
    background-color: #d9e5ff;
    display: grid;
    align-items: center;
    padding: 10px 0px;
    h1 {
    margin-bottom: 40px;
      text-align: center;
      z-index: 2;
      align-items: center;
      transform: translateY(25px);
      color: var(--fg-color-3);
      font-size: var(--size-medium);
      font-family: var(--primary-font);      
      span{        
        font-size: var(--size-xxl);
        color: inherit;
      }
    }
  }
</style>