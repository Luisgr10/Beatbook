const getState = ({ getStore, getActions, setStore }) => {
  return {
    store: {
      user: null,
      message: null,
      event: [],
      allEvents: [],
      allUsers: [],
      bands: [],
      places: [],
      demo: [
        {
          title: "FIRST",
          background: "white",
          initial: "white",
        },
        {
          title: "SECOND",
          background: "white",
          initial: "white",
        },
      ],
    },
    actions: {

      signUp: async (username, email, password, passwordConfirmation) => {
        try {
          const resp = await fetch(process.env.BACKEND_URL + "/api/sign_up", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              username: username,
              email: email,
              password: password,
              password_confirmation: passwordConfirmation,
            }),
          });
          const data = await resp.json();
          console.log(data);

          // Actualiza el estado global con la información del usuario
          setStore({ user: data });

          return data;
        } catch (error) {
          console.log("Error signing up", error);
        }
      },

      logIn: async (email, password) => {
        try {
          const resp = await fetch(process.env.BACKEND_URL + "/api/log_in", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              email: email,
              password: password,
            }),
          });

          if (!resp.ok) {
            throw new Error("Correo o contraseña no coinciden");
          }

          const data = await resp.json();
          // console.log(data);

          // Actualiza el estado global con la información del usuario
          setStore({ user: data });
          // Guarda el token en la localStorage
          // También deberías almacenar el usuario en la store utilizando la función setItem
          localStorage.setItem("jwt-token", data.token);

          return data;
        } catch (error) {
          console.log("Error logging in", error);
          throw error; // Asegúrate de volver a lanzar el error para que pueda ser capturado en tu componente
        }
        const user = setStore({ user }); // Obtén la información del usuario aquí...
      },

      logOut: () => {
        // Borra el objeto user del estado global
        setStore({ user: null });

        // Borra el token del almacenamiento local
        localStorage.removeItem("jwt-token");

        // Muestra un mensaje de éxito
        // toast.success("Has cerrado sesión correctamente");
      },

      getPrivateData: async () => {
        try {
          const token = localStorage.getItem("jwt-token");
          const resp = await fetch(process.env.BACKEND_URL + "/api/private", {
            method: "GET",
            headers: {
              Authorization: `Bearer ${token}`,
            },
          });

          if (resp.status === 401) {
            // El token no es válido o ha expirado
            localStorage.removeItem("jwt-token");
            setStore({ user: null });
            throw new Error("Token inválido o expirado");
          }

          if (!resp.ok) {
            throw new Error("Error al obtener datos privados");
          }

          const data = await resp.json();

          // Actualiza el estado global con la información obtenida
          setStore({ user: data });

          return data;
        } catch (error) {
          console.log("Error al obtener datos privados", error);
          throw error;
        }
      },

      createEvent: async (eventData) => {
        try {
          const token = localStorage.getItem("jwt-token"); // Obtén el token del almacenamiento local

          const response = await fetch(
            process.env.BACKEND_URL + "/api/events",
            {
              method: "POST",
              headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`, // Incluye el token en los headers
              },
              body: JSON.stringify(eventData),
            }
          );

          if (!response.ok) {
            throw new Error("Error creating event");
          }

          const data = await response.json();
          // console.log(data)
          // Aquí puedes actualizar tu store con la nueva información del evento si es necesario
          return data;
        } catch (error) {
          console.log("Error creating event", error);
        }
      },
      getEvents: async (searchTerm) => {
        const store = getStore();
        try {
          const resp = await fetch(process.env.BACKEND_URL + "/api/events");
          const data = await resp.json();
          setStore({ events: data });
          return data;
        } catch (error) {
          console.log("Error loading events from backend", error);
        }
      },

      getEvent: async (id) => {
        try {
          const resp = await fetch(
            process.env.BACKEND_URL + `/api/events/${id}`
          );
          const data = await resp.json();
          setStore({ event: data });
          return data;
        } catch (error) {
          console.log("Error loading event from backend", error);
        }
      },

      getAllEvents: async () => {
        try {
          const resp = await fetch(process.env.BACKEND_URL + "/api/events");
          if (!resp.ok) {
            throw new Error(`HTTP error! status: ${resp.status}`);
          }
          const data = await resp.json();

          setStore({ allEvents: data });

          return data;
        } catch (error) {
          console.log("Error loading users from backend", error);
          throw error;
        }
      },

      getAllUsers: async () => {
        try {
          const resp = await fetch(process.env.BACKEND_URL + "/api/users");
          if (!resp.ok) {
            throw new Error(`HTTP error! status: ${resp.status}`);
          }
          const data = await resp.json();

          // Actualiza el estado global con la información obtenida
          setStore({ allUsers: data });

          return data;
        } catch (error) {
          console.log("Error loading users from backend", error);
          throw error;
        }
      },

      getAllPlaces: async () => {
        try {
          const resp = await fetch(process.env.BACKEND_URL + "/api/places");
          if (!resp.ok) {
            throw new Error(`HTTP error! status: ${resp.status}`);
          }
          const places = await resp.json();
          return places;
        } catch (error) {
          console.log("Error loading places from backend", error);
        }
      },

      getAllBands: async () => {
        try {
          const resp = await fetch(process.env.BACKEND_URL + "/api/bands");
          if (!resp.ok) {
            throw new Error(`HTTP error! status: ${resp.status}`);
          }
          const data = await resp.json();

          setStore({ bands: data });
          return data;
        } catch (error) {
          console.log("Error loading bands from backend", error);
        }
      },

      getBand: async (bandId) => {
        try {
          const resp = await fetch(
            process.env.BACKEND_URL + "/api/bands/" + bandId
          );
          if (!resp.ok) {
            throw new Error(`HTTP error! status: ${resp.status}`);
          }
          const band = await resp.json();
          return band;
        } catch (error) {
          console.log("Error loading band from backend", error);
          throw error;
        }
      },
      uploadEventPicture: async (image) => {
        console.log("uploadEventPicture se ha llamado"); // Nuevo registro de consola
        try {
          const token = localStorage.getItem("jwt-token");
          const formData = new FormData();
          formData.append("image", image);

          console.log("Subiendo imagen con token:", token); // Nuevo registro de consola

          const response = await fetch(
            process.env.BACKEND_URL + "/api/upload_event_picture",
            {
              method: "POST",
              headers: {
                Authorization: `Bearer ${token}`,
              },
              body: formData,
            }
          );
          console.log(image);
          if (!response.ok) {
            throw new Error("Error uploading event picture");
          }

          const data = await response.json();
          console.log("Respuesta del servidor:", data); // Nuevo registro de consola
          console.log("URL de la imagen:", data.url); // Nuevo registro de consola

          // Asegúrate de que estás devolviendo un objeto con una propiedad url
          return { url: data.url };
        } catch (error) {
          console.log("Error uploading event picture", error);
        }
      },

      uploadEventMedia: async (files, eventId) => {
        try {
          const token = localStorage.getItem("jwt-token");

          const formData = new FormData();
          for (const file of files) {
            formData.append("images", file); // Asegúrate de que el servidor espera "images" como el nombre del campo para los archivos
          }
          formData.append("event_id", eventId); // Asegúrate de que el servidor espera "event_id" como el nombre del campo para el id del evento

          const response = await fetch(
            process.env.BACKEND_URL + "/api/upload_event_media",
            {
              method: "POST",
              headers: {
                Authorization: `Bearer ${token}`,
              },
              body: formData,
            }
          );

          if (!response.ok) {
            const errorData = await response.json(); // Intenta obtener más información sobre el error del cuerpo de la respuesta
            throw new Error("Error uploading event media: " + JSON.stringify(errorData));
          }

          const data = await response.json();
          console.log(data);

          // Asegúrate de que estás devolviendo un objeto con una propiedad urls que es un array
          return { urls: data.urls };
        } catch (error) {
          console.log("Error uploading event media", error);
        }
      },
    },
  };
};

export default getState;
