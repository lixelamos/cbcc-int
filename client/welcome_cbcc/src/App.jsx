
import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    age: '',
    phone_number: '',
    email: '',
    gprs_location: '',
    profile_picture: ''
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('/api/register', formData)
      .then(response => {
        console.log(response.data.message);
      })
      .catch(error => {
        console.error('Error:', error);
      });
  };

  return (
    <div>
      <h1>User Registration</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" name="first_name" placeholder="First Name" onChange={handleChange} />
        <input type="text" name="last_name" placeholder="Last Name" onChange={handleChange} />
        <input type="number" name="age" placeholder="Age" onChange={handleChange} />
        <input type="text" name="phone_number" placeholder="Phone Number" onChange={handleChange} />
        <input type="email" name="email" placeholder="Email" onChange={handleChange} />
        <input type="text" name="gprs_location" placeholder="GPRS Location" onChange={handleChange} />
        <input type="file" name="profile_picture" onChange={handleChange} />
        <button type="submit">Register</button>
      </form>
    </div>
  );
}

export default App;
