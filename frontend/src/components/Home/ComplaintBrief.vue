<template>
    <div style="margin: 10px">
        <span>I am complaint brief, ahaha.</span>

        <b-button v-b-modal="`complaint-modal-${complaintid}`" variant="outline-secondary">Show more</b-button>
        <b-modal :id="`complaint-modal-${complaintid}`" size='lg' hide-header	>
            <ComplaintModal></ComplaintModal>

        </b-modal>
    </div>
</template>



<script>
import ComplaintModal from '@/components/ComplaintModal.vue';


    export default {
        components: {
            ComplaintModal
        },
        props: ['complaintid']
    }
</script>

<style lang="scss" scoped>

</style>