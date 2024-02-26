<script setup lang="ts">
import {ref,computed} from 'vue'
interface Props{    
    rotate:number;
}
const props = defineProps<Props>()
const rotate = ref(props.rotate)
const startY = ref(0)
const rotateProperty = computed(()=>{
    return `${rotate.value}deg`;
})
const elementInView = (el:HTMLElement, percentageScroll = 100) => {
  const elementTop = el.getBoundingClientRect().top;
  return (
    elementTop <= 
    ((window.innerHeight || document.documentElement.clientHeight) * (percentageScroll/100))
  );
};

const handleScrollAnimation = () => {
    
    var scrollY = window.scrollY;
    var scrollDown= scrollY >startY.value
    startY.value = scrollY
    let delta = scrollDown?-1:1
    const element = document.querySelector(".rotate-el") as HTMLElement
    if (elementInView(element, 100)) {
      rotate.value += delta;
    } else {
    //   hideScrollElement(el);
    }

}
document.addEventListener("scroll",handleScrollAnimation);
</script>
<template>    
      
        <Transition>            
            <div  class="rotate-el">      
                <slot></slot>                        
            </div>
        </Transition>
    
</template>
<style >
.rotate-el{
    transform: rotateZ(v-bind(rotateProperty));
}
.v-enter-active,
.v-leave-active {
  transition: rotate 0.5s ease;
}

.v-enter-from,
.v-leave-to {
  rotate: 0 0 1 v-bind(rotateProperty);
}

</style>