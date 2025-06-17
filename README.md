
Prueba técnica – CFT (Full Stack)

Este proyecto está dividido en dos partes principales:

- **Backend:** API REST construida en Python con FastAPI y MongoDB.
- **Frontend:** Interfaz en React con Material UI, conectada al backend para realizar un CRUD completo.

---

🚀 Cómo iniciar el proyecto

Requisitos

- Python 3.10+
- Node.js v18+
- MongoDB Atlas o local
- Docker (opcional)

 Backend

1. Instalar dependencias:

cd backend
python -m venv venv
source venv/bin/activate  # o .\venv\Scripts\activate en Windows
pip install -r requirements.txt


Crear archivo .env con la URI de MongoDB:

.env
MONGO_URI=mongodb://root:6PaoFsr77wzl@57.129.59.106:27017/?authSource=admin

Ejecutar el backend:
uvicorn main:app --reload

Frontend
Instalar dependencias:
cd frontend
npm install

Iniciar el frontend:
npm run dev









1. ¿Qué pasa si un usuario tiene un campo mal nombrado en la base de datos?
	•	En MongoDB: se puede hacer un updateMany para renombrar el campo sin afectar el resto de datos. Algo como:

db.usuarios.updateMany(
  { nombre_antiguo: { $exists: true } },
  [
    { $set: { nombre_nuevo: "$nombre_antiguo" } },
    { $unset: "nombre_antiguo" }
  ]
)

En MySQL: simplemente se puede usar ALTER TABLE para cambiar el nombre de la columna:

ALTER TABLE usuarios CHANGE nombre_antiguo nombre_nuevo VARCHAR(255);

2. Añadir un campo nuevo sin apagar el sistema

Para no romper nada, lo ideal sería:
	1.	Añadir el campo como opcional o con un valor por defecto (por ejemplo, NULL en SQL).
	2.	No exigirlo en la lógica del backend de entrada (aún).
	3.	Hacer deploy sin afectar la funcionalidad actual.
	4.	Ir poblando ese campo si hace falta (por ejemplo, con un script o a medida que los usuarios actualizan).
	5.	Finalmente, cuando todo esté listo, usarlo de forma activa en el sistema.

3. Integrar un nuevo servidor
	1.	Ver qué papel va a tener ese servidor (espejo, escalar tráfico, backup, etc.).
	2.	Elegir un proveedor cloud confiable (AWS, GCP, Azure…) y configurar red, firewall, llaves SSH, etc.
	3.	Configurar actualizaciones automáticas, logs centralizados y monitoreo (tipo Prometheus, Grafana).
	4.	Añadirlo al balanceador de carga y comprobar que responde bien.
	5.	Hacer pruebas de rendimiento y seguridad antes de ponerlo 100% operativo.

4. El sistema se cae completamente y no se sabe por qué
	1.	Lo primero: revisar logs, métricas, y monitoreo para entender qué pasó.
	2.	Mirar si hubo algún cambio reciente o despliegue que lo haya provocado.
	3.	Si hay rollback posible, hacerlo.
	4.	Si no, levantar el sistema por partes para aislar el problema.
	5.	Documentar el fallo y aplicar mejoras para que no se repita (alertas, backups, etc.).

5. ¿Qué harías ante una brecha de seguridad?
	1.	Aislar inmediatamente el sistema o servicio afectado.
	2.	Informar al equipo técnico y de seguridad.
	3.	Revisar logs, accesos y actividades recientes.
	4.	Cambiar credenciales, revocar accesos y aplicar parches si hace falta.
	5.	Comunicar a usuarios si se han visto afectados.
	6.	Documentar todo y reforzar medidas de prevención a futuro.

Parte 4 – Diseño e integraciones

¿Qué patrones de diseño aplicarías en MySQL?
	•	Normalización: para no duplicar datos innecesariamente.
	•	Foreign keys: para asegurar que las relaciones entre tablas tengan sentido.
	•	Índices: para acelerar consultas.
	•	Partitioning: si la base de datos se pone muy grande.
	•	Read replicas: para repartir la carga si hay muchas lecturas.


¿Qué patrones de diseño aplicarías en MongoDB?
	•	Embebido de documentos (embedding): cuando hay relaciones 1:N y se accede todo junto.
	•	Referencias: útil para relaciones más complejas o si los documentos se vuelven muy grandes.
	•	Soft deletes: usando campos como deletedAt o isDeleted en vez de borrar directamente.
	•	Colecciones limitadas (capped): por ejemplo para logs o sistemas FIFO.
	•	Sharding: si se espera escalar horizontalmente.


¿Qué patrones usaste o usarías en proyectos anteriores?
	•	Repository Pattern: para tener bien separado el acceso a datos del resto de la app.
	•	Service Layer: para mantener la lógica de negocio clara y reutilizable.
	•	DTOs (Data Transfer Objects): para definir exactamente qué se intercambia entre backend y frontend.
	•	Factory Pattern: cuando se necesita crear objetos dinámicamente dependiendo del contexto (por ejemplo, tipos de usuarios).
	•	MVC: estructura básica pero muy útil, especialmente en proyectos web.


¿Cómo automatizarías un sistema de microservicios?
	•	Cada servicio en su propio contenedor con Docker.
	•	Orquestación con Docker Compose (desarrollo) o Kubernetes (producción).
	•	Pipelines CI/CD para testear, construir y desplegar automáticamente.
	•	Logs y métricas centralizadas.
	•	Configuración externa y segura usando variables de entorno o servicios como Vault.


¿Qué métodos de seguridad aplicarías?
	•	Cifrado de tráfico con HTTPS.
	•	Autenticación con JWT o OAuth.
	•	Control de acceso por roles (RBAC).
	•	Hash de contraseñas con bcrypt.
	•	Validaciones contra inyecciones (SQL, NoSQL).
	•	Rate limiting para evitar ataques de fuerza bruta.
	•	Backups cifrados y acceso a infraestructura solo con SSH + VPN si es necesario.


¿Qué flujos de conexión a base de datos aplicaste?
	•	Conexiones persistentes y pooling para mejorar rendimiento.
	•	Variables de entorno para manejar credenciales según el entorno (dev, prod, etc.).
	•	Reintentos automáticos en casos de fallos temporales.
	•	Logs de consultas lentas para poder optimizar cuando haga falta.
	•	Cierre limpio de conexiones al finalizar procesos.


¿Qué flujos de CI/CD has usado y cómo los aplicarías?
	•	Uso de GitHub Actions o similar para correr tests, linters y build en cada push.
	•	Automatización del build de imágenes Docker.
	•	Deploy automático a entornos de staging, y manual a producción tras aprobación.
	•	Escaneo de vulnerabilidades antes de hacer deploy.
	•	Notificaciones por Slack o Email cuando algo falla o sale bien.
