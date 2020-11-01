<template>
    <form v-on:submit.prevent="onSubmit">
        <input class="main-input" type="text" id="new-todo-input" name="new-todo" autocomplete="off" v-model.trim="title" placeholder="Title">
        <input class="main-input" type="date" name="new-todo" autocomplete="off" v-model.trim="dueDate">
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
            this.$emit('todo-added', this.title, this.dueDate);
            this.title = '';
            this.dueDate = ''
        },
    },
    data() {
        return {
            title: "",
            dueDate: "",
        }
    }
}
</script>