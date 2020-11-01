<template>
    <div v-if="!isEditing">
        <input v-on:change="$emit('checkbox-changed')" type="checkbox" v-bind:id="id" v-bind:checked="isDone"/>
        <label v-bind:for="id">{{ title }} {{ transformDate(dueDate) }}</label>
        <button type="button" v-on:click="toogledToEditForm">Edit</button>
        <button type="button" v-on:click="deleteToDo">Delete</button>
        <!-- <img src='@/assets/trash.png' alt='some' width="20" height="20"> -->
    </div>
    <to-do-edit-form v-else v-on:item-edited="itemEdited" v-bind:id="id" v-bind:title="title"></to-do-edit-form>

</template>

<script>
import moment from 'moment';
import ToDoEditForm from './ToDoEditForm'

export default {
    components: {
        ToDoEditForm
    },

    props: {
        id: {required: true},
        title: {required: true, type: String},
        description: {required: false, type: String},
        dueDate: {required: false, type: String},
        isDone: {required: true, type: Boolean},
    },

    methods: {
        transformDate(value) {
            return moment(String(value)).format('MM/DD/YYYY hh:mm')
        },

        toogledToEditForm() {
            this.isEditing = true;
        },

        deleteToDo() {
            this.$emit('item-deleted');
        },

        itemEdited(newTitle) {
            this.$emit('item-is-edited', newTitle);
            this.isEditing = false;
        }
    },

    data() {
        return {
            isEditing: false
        }
    }
}
</script>

<style scoped>
</style>