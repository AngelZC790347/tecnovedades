<script setup lang="ts">
import {ref,computed} from 'vue'
import Scrollbar from "smooth-scrollbar"
interface Props{    
    rotate:number;
    threshold:number;      
    scale:number;    
}
const props = defineProps<Props>()
const rotate = ref(props.rotate)
const scale = ref(props.scale)
const startY = ref(0)
const rotateProperty = computed(()=>{
    return `${rotate.value}deg`;
})

const scroll =  Scrollbar.get(document.getElementById("my-scrollbar")!)
const currentYOfset = ref(scroll?.offset.y)
const elementInView = ( percentageScroll = 100) => {        
    console.log(scroll?.isVisible(document.getElementById("animated-el-rotated")!));    
    return (        
     scroll?.isVisible(document.getElementById("animated-el-rotated")!)
    );
};
const handleScrollAnimation = () => {
    var scrollY = scroll?.offset.y!;    
    var scrollDown= scrollY >startY.value
    console.log(scrollY); 
    console.log(currentYOfset.value);       
    startY.value = scrollY    
    let deltaScroll = scrollDown?-Math.abs((scrollY - currentYOfset.value!)/20):Math.abs((scrollY - currentYOfset.value!)/20)    
    console.log(deltaScroll);    
    const element = document.querySelector(".rotate-el") as HTMLElement
    if (elementInView(80)) {
        console.log("inview");  
        if(Math.abs(rotate.value+deltaScroll) <= props.threshold){
            rotate.value += deltaScroll;        
        }               
    }
    currentYOfset.value = scrollY
    console.log(rotate.value);   
}
scroll?.addListener(handleScrollAnimation)


</script>
<template>    
      
        <Transition>            
            <div  id="animated-el-rotated" class="rotate-el">      
                <slot></slot>                        
            </div>
        </Transition>
    
</template>
<style >
.rotate-el{
    transform: rotateZ(v-bind(rotateProperty)) scale(v-bind(scale));    

}
.v-enter-active,
.v-leave-active {
  transition: rotate scale 1.5s ease;
}

.v-enter-from,
.v-leave-to {
    transform: rotateZ(v-bind(rotateProperty)) scale(v-bind(scale));    
}

</style>