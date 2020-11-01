<template>
  <div>
    <to-do-form v-on:todo-added="createToDo"></to-do-form>
    <p>{{ listSummary }}</p>
    <ul>
      <li v-for="item in toDoItems" v-bind:key="item.id">
        <to-do-item v-on:item-deleted="deleteToDo(item.id)" v-on:item-is-edited="itemIsEdited(item.id, $event)" v-on:checkbox-changed="updateDoneStatus(item.id)" v-bind:id="item.id" v-bind:isDone="item.is_done" v-bind:title="item.name" v-bind:dueDate="item.due_date"></to-do-item>
      </li>
    </ul>
  </div> 
</template>

<script>
import ToDoItem from './components/ToDoItem.vue';
import ToDoForm from './components/ToDoForm.vue';

export default {
  name: 'App',
  components: {
    ToDoItem,
    ToDoForm
  },

  async created() {
    this.getToDo()
  },

  data() {
    return {
      toDoItems: [],
    }
  },

  computed: {
    listSummary() {
      const doneTasks = this.toDoItems.filter(item => item.is_done);
      return `${doneTasks.length} out of ${this.toDoItems.length} completed`;
    }
  },

  methods: {

    async getToDo() {
      let dataFromApi = await fetch('http://127.0.0.1:8000/api/tasks/');
      this.toDoItems = await dataFromApi.json();
    },

    async createToDo(title, description, date) {
      await fetch('http://127.0.0.1:8000/api/tasks/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({name: title, description: description, due_date: date})
      });
      this.getToDo();
    },

    async deleteToDo(toDoId) {
      await fetch(`http://127.0.0.1:8000/api/tasks/${toDoId}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json'
        },
      });
      this.getToDo();
    },

    async updateDoneStatus(toDoId) {
      const updatedItem = this.toDoItems.filter(item => item.id === toDoId)
      updatedItem[0].is_done = !updatedItem[0].is_done
      await fetch(`http://127.0.0.1:8000/api/tasks/${toDoId}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({is_done: updatedItem[0].is_done})
      });
      this.getToDo();
    },

    async itemIsEdited(toDoId, newTitle) {
      await fetch(`http://127.0.0.1:8000/api/tasks/${toDoId}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({name: newTitle})
      });
      this.getToDo();
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

ul {
     list-style: none;
     box-shadow: 0 0 10px rgba(0,0,0,0.5);
     width: 35%;
     margin-left: auto;
     margin-right: auto;
     padding: 0px;
 }

li {
  padding: 20px 0px;
  border-bottom: 1px solid lightgray;
}

img {
  vertical-align: middle;
}

</style>
