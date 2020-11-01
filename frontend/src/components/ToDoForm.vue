<template>
    <form v-on:submit.prevent="onSubmit">
        <input type="text" id="new-todo-input" name="new-todo" autocomplete="off" v-model.trim="title" placeholder="name">
        <input type="text" name="new-todo" autocomplete="off" v-model.trim="description" placeholder="description">
        <input type="datetime-local" name="new-todo" autocomplete="off" v-model.trim="dueDate" placeholder="Due date">
        <button type="submit">Add</button>
    </form>
</template>

<script>
export default {
    methods: {
        onSubmit() {
            if (this.title === ''){
                return
            }
            this.$emit('todo-added', this.title, this.description, this.dueDate);
            this.title = '';
            this.description = '';
            this.dueDate = ''
        },
    },
    data() {
        return {
            title: "",
            description: "",
            dueDate: "",
        }
    }
}
</script>