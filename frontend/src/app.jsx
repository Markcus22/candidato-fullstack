import React, { useEffect, useState } from "react";
import {
  AppBar, Toolbar, Typography, Container, Paper, TextField, Button, List, ListItem, ListItemText, Box
} from "@mui/material";
import { getUsers, createUser } from "./api";

function App() {
  const [users, setUsers] = useState([]);
  const [form, setForm] = useState({ username: "", email: "", password: "" });
  const [error, setError] = useState("");

  useEffect(() => {
    getUsers().then(setUsers);
  }, []);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
    setError("");
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!form.username || !form.email || !form.password) {
      setError("Todos los campos son obligatorios.");
      return;
    }
    try {
      await createUser(form);
      setUsers(await getUsers());
      setForm({ username: "", email: "", password: "" });
    } catch {
      setError("Error al crear usuario.");
    }
  };

  return (
    <Box sx={{ bgcolor: "#f4f6f8", minHeight: "100vh" }}>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6">Gestión de Usuarios</Typography>
        </Toolbar>
      </AppBar>
      <Container maxWidth="sm" sx={{ mt: 4 }}>
        <Paper sx={{ p: 3, mb: 3 }}>
          <Typography variant="h5" gutterBottom>Crear usuario</Typography>
          <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: 16 }}>
            <TextField
              label="Nombre de usuario"
              name="username"
              value={form.username}
            onChange={handleChange}
              required
            />
            <TextField
              label="Correo electrónico"
              name="email"
              type="email"
              value={form.email}
              onChange={handleChange}
              required
            />
            <TextField
              label="Contraseña"
              name="password"
              type="password"
              value={form.password}
              onChange={handleChange}
              required
            />
            <Button type="submit" variant="contained" color="primary">
              Crear usuario
            </Button>
            {error && <Typography color="error">{error}</Typography>}
          </form>
        </Paper>
        <Paper sx={{ p: 3 }}>
          <Typography variant="h5" gutterBottom>Usuarios registrados</Typography>
          <List>
            {users.map((user) => (
              <ListItem key={user._id} divider>
                <ListItemText primary={user.username} secondary={user.email} />
              </ListItem>
            ))}
          </List>
        </Paper>
      </Container>
    </Box>
  );
}

export default App;