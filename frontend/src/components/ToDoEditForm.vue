<template>
    <form v-on:submit.prevent="onSubmit">
        <div>
            <span>
                <label>Edit title</label>
                <input class="main-input" type="text" autocomplete="off" v-model.trim="newTitle"/>
            </span>
            <span>
                <button type="submit">Save</button>
                <button type="button" v-on:click="onCancel">Cancel</button>
            </span>
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
        },

        onCancel() {
            this.$emit('edit-cancelled')
        }
    }
}
</script>