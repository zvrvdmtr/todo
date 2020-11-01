<template>
    <div v-if="!isEditing">
        <span>
            <input v-on:change="$emit('checkbox-changed')" type="checkbox" v-bind:id="id" v-bind:checked="isDone"/>
            <label class="main-title" v-bind:for="id">{{ title }}</label>
        </span>
        <span class="date">{{ transformDate(dueDate) }}</span>
        <span>
            <button type="button" v-on:click="toogledToEditForm">Edit</button>
            <button type="button" v-on:click="deleteToDo">Delete</button>
        </span>
    </div>
    <to-do-edit-form v-else v-on:edit-cancelled="editCancelled" v-on:item-edited="itemEdited" v-bind:id="id" v-bind:title="title"></to-do-edit-form>

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
        dueDate: {required: false, type: String},
        isDone: {required: true, type: Boolean},
    },

    methods: {
        transformDate(value) {
            return moment(String(value)).format('MM/DD/YYYY')
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
        },

        editCancelled() {
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