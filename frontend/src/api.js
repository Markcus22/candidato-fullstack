import axios from "axios";

const API = "http://localhost:8000";

// Obtener usuarios
export const getUsers = async () => {
  const res = await axios.get(`${API}/users`);
  return res.data;
};

// Crear usuario
export const createUser = async (user) => {
  const res = await axios.post(`${API}/users`, user);
  return res.data;
};