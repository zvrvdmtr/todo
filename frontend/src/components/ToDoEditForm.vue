<template>
    <form v-on:submit.prevent="onSubmit">
        <div>
            <label>Edit title for {{ title }}</label>
            <input type="text" autocomplete="off" v-model.trim="newTitle"/>
            <button type="submit">Save</button>
        </div>
    </form>    
</template>

<script>
export default {
    props: {
        id: {requiredL: true},
        title: {required: true, type: String}
    },

    data() {
        return {
            newTitle: this.title
        }
    },

    methods: {
        onSubmit() {
            if (this.newTitle && this.newTitle != this.title) {
                this.$emit('item-edited', this.newTitle)
            }
        }
    }
}
</script>