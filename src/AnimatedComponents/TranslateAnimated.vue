<script setup lang="ts">
import {ref,computed} from 'vue'
import Scrollbar from "smooth-scrollbar"
interface Props{    
    translateX:number;
}
const props = defineProps<Props>()
const translateX = ref(props.translateX)
const startY = ref(0)
const translateXProperty = computed(()=>{
    return `${translateX.value}px`;
})

const scroll =  Scrollbar.get(document.getElementById("my-scrollbar")!)
const currentYOfset = ref(scroll?.offset.y)
const elementInView = ( percentageScroll = 100) => {        
    console.log(scroll?.isVisible(document.getElementById("animated-el-translateXd")!));    
    return (        
     scroll?.isVisible(document.getElementById("animated-el-translateXd")!)
    );
};
// const handleScrollAnimation = () => {
//     var scrollY = scroll?.offset.y!;    
//     var scrollDown= scrollY >startY.value
//     console.log(scrollY); 
//     console.log(currentYOfset.value);       
//     startY.value = scrollY    
//     let deltaScroll = scrollDown?-Math.abs((scrollY - currentYOfset.value!)*props.multiplier):Math.abs((scrollY - currentYOfset.value!)*props.multiplier)    
//     console.log(deltaScroll);        
//     if (elementInView(80)) {        
//         console.log("inview");  
//         if(Math.abs(translateX.value+deltaScroll) <= props.threshold){
//             translateX.value += deltaScroll;        
//         }               
//     }
//     currentYOfset.value = scrollY
//     console.log(translateX.value);   
// }
// scroll?.addListener(handleScrollAnimation)


</script>
<template>
        <Transition name="rotated">            
            <div  id="animated-el-rotated" class="rotate-el">      
                <slot></slot>                        
            </div>
        </Transition>
    
</template>
<style scoped>
.rotate-el{
    transform: translateX(v-bind(translateXProperty));    

}
.rotated-enter-active,
.rotated-leave-active {
  transition: translateX scale 1.5s ease;
}

.rotated-enter-from,
.rotated-leave-to {
    transform: translateX(v-bind(translateXProperty)) ;    
}

</style>