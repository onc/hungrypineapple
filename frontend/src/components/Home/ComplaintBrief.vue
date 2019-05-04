<template>
    <div class="complaint-brief-div">
        <b-row>
            <b-col cols="1" class='status my-auto'>
                <svg style="width:20px; height:20px;"><circle cx=8 cy=8 r=8 fill='black'></circle></svg>
            </b-col>
            <b-col cols="7" class="complaint-title my-auto"><span>I am complaint brief, ahaha.</span></b-col>
            <b-col cols="2" class="voting-buttons my-auto">Voting</b-col>
            <b-col cols="2" class="show-me-button my-auto">
                <b-button v-b-modal="`complaint-modal-${complaintid}`" variant="outline-secondary">Show more</b-button>
                <b-modal :id="`complaint-modal-${complaintid}`" size='lg' hide-header><ComplaintModal></ComplaintModal>

        </b-modal>
            </b-col>
        </b-row>
        

        
            
    </div>
</template>



<script>
import ComplaintModal from '@/components/ComplaintModal.vue';


    export default {
        components: {
            ComplaintModal
        },
        props: ['complaintid', 'complaint']
    }
</script>

<style scoped>

.complaint-brief-div {
    margin: 10px; 
    background-color:white;
}

</style>