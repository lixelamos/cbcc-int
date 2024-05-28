import React, { useState } from "react";
import styled from "styled-components";
import { mobile } from "../responsive";

const Container = styled.div`
  width: 100vw;
  height: 100vh;
  background: linear-gradient(
      rgba(255, 255, 255, 0.5),
      rgba(255, 255, 255, 0.5)
    ),
      center;
  background-size: cover;
  display: flex;
  align-items: center;
  justify-content: center;
`;

const Wrapper = styled.div`
  width: 40%;
  padding: 20px;
  background-color: white;
  ${mobile({ width: "75%" })}
`;

const Title = styled.h1`
  font-size: 24px;
  font-weight: 300;
`;

const Form = styled.form`
  display: flex;
  flex-wrap: wrap;
`;

const Input = styled.input`
  flex: 1;
  min-width: 40%;
  margin: 20px 10px 0px 0px;
  padding: 10px;
`;

const Agreement = styled.span`
  font-size: 12px;
  margin: 20px 0px;
`;

const Button = styled.button`
  width: 40%;
  border: none;
  padding: 15px 20px;
  background-color: teal;
  color: white;
  cursor: pointer;
`;

const Register = () => {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [age, setAge] = useState("");
  const [phoneNumber, setPhoneNumber] = useState("");
  const [email, setEmail] = useState("");
  const [gprsLocation, setGprsLocation] = useState("");
  const [error, setError] = useState("");

  const handleRegister = async (e) => {
    e.preventDefault();
    setError(""); // Clear any previous error message

    // Validate input (you can add more validation if needed)
    if (!firstName || !lastName || !age || !phoneNumber || !email || !gprsLocation) {
        setError("Please fill in all fields.");
        return;
    }

    const userData = {
        first_name: firstName,
        last_name: lastName,
        age: age,
        phone_number: phoneNumber,
        email: email,
        gprs_location: gprsLocation
    };

    try {
        const response = await fetch("http://localhost:5555/api/register/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(userData)
        });

        if (response.ok) {
            // Handle successful registration (e.g., redirect to another page)
            console.log("Registration successful");
        } else {
            // Handle registration error
            const data = await response.json();
            setError(data.message || "Registration failed. Please try again.");
        }
    } catch (error) {
        console.error("Error:", error);
        setError("An error occurred while registering. Please try again later.");
    }
};


  return (
    <Container>
      <Wrapper>
        <Title>Register</Title>
        <Form>
          <Input placeholder="First Name" value={firstName} onChange={(e) => setFirstName(e.target.value)} />
          <Input placeholder="Last Name" value={lastName} onChange={(e) => setLastName(e.target.value)} />
          <Input placeholder="Age" value={age} onChange={(e) => setAge(e.target.value)} />
          <Input placeholder="Phone Number" value={phoneNumber} onChange={(e) => setPhoneNumber(e.target.value)} />
          <Input placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
          <Input placeholder="GPRS Location" value={gprsLocation} onChange={(e) => setGprsLocation(e.target.value)} />
          <Agreement>
            By creating an account, I consent to the processing of my personal
            data in accordance with the <b>PRIVACY POLICY</b>
          </Agreement>
          <Button onClick={handleRegister}>Register</Button>
          {error && <span style={{ color: "red" }}>{error}</span>}
        </Form>
      </Wrapper>
    </Container>
  );
};

export default Register;
