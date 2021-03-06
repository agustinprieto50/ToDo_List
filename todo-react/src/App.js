import React from 'react';
import './App.css';


class App extends React.Component {

  constructor(props){
    super(props);
      this.state = {
        todoList:[],
        activeItem:{
          id: null,
          title: '',
          completed:false,
        },
        editing:false,
      }
      this.fetchTasks = this.fetchTasks.bind(this)
      this.handleChange = this.handleChange.bind(this)
      this.handleSubmit = this.handleSubmit.bind(this)
      // this.getCookie = this.getCookie.bind(this)
      this.delete = this.delete.bind(this)
      this.startEdit = this.startEdit.bind(this)
      this.strikeUnstrike = this.strikeUnstrike.bind(this)

  };

//   getCookie(name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         const cookies = document.cookie.split(';');
//         for (let i = 0; i < cookies.length; i++) {
//             const cookie = cookies[i].trim();
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }

  componentDidMount(){
    this.fetchTasks()
  }
  fetchTasks(){
    fetch('http://127.0.0.1:8000/api/tasklist/')
    .then(response => response.json())
    .then(data =>
      this.setState({
        todoList:data
      })
      )
  }

  handleChange(e){
    var name = e.target.name
    var value = e.target.value
    console.log('name:', name )
    console.log('value:', value )
    this.setState({
      activeItem:{
        ...this.state.activeItem,
        name:value
      }
    })
  }

  handleSubmit(e){
    e.preventDefault()
    console.log('ITEM:', this.state.activeItem)
  
    // const csrftoken = this.getCookie('csrftoken');

    var url = "http://127.0.0.1:8000/api/createtask/"

    if(this.state.editing == true){
      url = `http://127.0.0.1:8000/api/edittask/${this.state.activeItem.id}/`
      this.setState({
        editing:false
      })
    }

    fetch(url, {
      'method': 'POST',
      'headers':{
        'Content-type': 'application/json',
        // 'X-CSFRToken':csrftoken
      },
      body:JSON.stringify(this.state.activeItem)
    }).then((response) =>{
      this.fetchTasks()
      this.setState({
        activeItem:{
          id: null,
          name: '',
          completed:false,
        }
      })
    }).catch(function(error){
      console.log('ERROR:', error)
    })
  }

  startEdit(task){
    this.setState({
      activeItem: task,
      editing: true,
    })
  }

  delete(task){
    var url = `http://127.0.0.1:8000/api/deletetask/${task.id}/`
    fetch(url, {
      'method': 'DELETE',
      'headers':{
        'Content-type':'application/json',
        // 'X-CSFRToken':csrftoken
      },
  }).then((response) => {
    this.fetchTasks()
  })
}

strikeUnstrike(task){
  task.isCompleted = !task.isCompleted
  var url = `http://127.0.0.1:8000/api/edittask/${task.id}/`
  fetch(url, {
    method: 'POST',
    headers:{
      'Content-type':'application/json',
      // 'X-CSFRToken':csrftoken
    },
    body:JSON.stringify({'isCompleted': task.isCompleted, 'name':task.name})
}).then(() => {
  this.fetchTasks()
})
  
}

  render(){
    var tasks = this.state.todoList
    var self = this

    return(
      <div className="container">
        <div id="task-container">
          <div id='form-wrapper'>
            <form onSubmit={this.handleSubmit} id="form">
              <div className="flex-wrapper">
                <div style={{flex:6}}>
                  <input onChange={this.handleChange} className="form-control" id="title" value={this.state.activeItem.name} name="title" placeholder="Add a task"></input>
                </div>
                <div style={{flex:1}}>
                  <input className="btn btn-warning" id="submit" type="submit" name='Add'></input>
                </div>
              </div>
            </form>
          </div>
          <div id="list-wrapper">
            {tasks.map(function(task, index){
              return(
                <div key={index} className="task-wrapper flex-wrapper">

                  <div onClick={() => self.strikeUnstrike(task)} style={{flex:7}}>
                    {task.isCompleted == false ?(
                      <span>{task.name}</span>
                    ) : (
                      <strike>{task.name}</strike>
                    )}
                    
                  </div>

                  <div style={{flex:1}}>
                    <button onClick={() => self.startEdit(task)} className='btn btn-sm btn-outline-info'>Edit</button>
                  </div>

                  <div style={{flex:1}}>
                    <button onClick={() => self.delete(task)} className='btn btn-sm btn-outline-dark delete'>Delete</button>
                  </div>

                </div>
              )
            })}
          </div>
        </div>
      </div>
    )
  }
}

export default App;
