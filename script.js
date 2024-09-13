const todoForm = document.getElementById('todo-form');
const todoList = document.getElementById('todo-list');

todoForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;

    const response = await fetch('/todos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title, description })
    });

    if (response.ok) {
        const data = await response.json();
        console.log(data.message);
        location.reload();
    } else {
        const errorData = await response.json();
        console.error(errorData.error);
    }
});

todoList.addEventListener('click', async (event) => {
    if (event.target.classList.contains('delete-button')) {
        const todoId = event.target.dataset.id;

        const response = await fetch(`/todos/${todoId}`, {
            method: 'DELETE'
        });

        if (response.ok) {
            console.log('Todo deleted successfully');
            location.reload();
        } else {
            console.error('Error deleting todo');
        }
    }
}); 

// ... rest of your JavaScript code

// Add event listener for hover effect
todoList.addEventListener('mouseover', (event) => {
    const liElement = event.target.closest('li');
    if (liElement) {
        const descriptionElement = liElement.querySelector('.todo-description');
        descriptionElement.style.display = 'block';
    }
});

todoList.addEventListener('mouseout', (event) => {
    const liElement = event.target.closest('li');
    if (liElement) {
        const descriptionElement = liElement.querySelector('.todo-description');
        descriptionElement.style.display = 'none';
    }
});