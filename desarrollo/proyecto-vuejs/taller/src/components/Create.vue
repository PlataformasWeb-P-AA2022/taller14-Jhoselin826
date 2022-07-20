<template>
    <div class="pt-5">
        <form @submit.prevent="create" method="post">
            <div class="form-group">
                <label for="nombre">Nombre</label>
                <input
                    type="text"
                    class="form-control"
                    id="nombre"
                    v-model="propietario.nombre"
                    v-validate="'required'"
                    name="nombre"
                    placeholder="Ingres su nombre"
                    :class="{'is-invalid': errors.has('propietario.nombre') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid name.
                </div>
            </div>

            <div class="form-group">
                <label for="apellido">Apellido</label>
                <input
                    type="text"
                    class="form-control"
                    id="nombre"
                    v-model="propietario.apellido"
                    v-validate="'required'"
                    name="apellido"
                    placeholder="Ingrese su apellido"
                    :class="{'is-invalid': errors.has('propietario.apellido') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid apellido.
                </div>
            </div>

            <div class="form-group">
                <label for="edad">Edad</label>
                <input
                    type="text"
                    class="form-control"
                    id="edad"
                    v-model="propietario.edad"
                    v-validate="'required'"
                    name="apellido"
                    placeholder="Ingrese su edad"
                    :class="{'is-invalid': errors.has('propietario.edad') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid edad.
                </div>
            </div>

            <div class="form-group">
                <label for="nacionalidad">Nacionalidad</label>
                <input
                    type="text"
                    class="form-control"
                    id="nacionalidad"
                    v-model="propietario.nacionalidad"
                    v-validate="'required'"
                    name="apellido"
                    placeholder="Ingrese su nacionalidad"
                    :class="{'is-invalid': errors.has('propietario.nacionalidad') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid nacionalidad.
                </div>
            </div>
            <button type="submit" class="btn btn-primary">Crear</button>
        </form>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    data() {
        return {
            propietario: {
                nombre: '',
                apellido: '',
                edad: '',
                nacionalidad: '',
            },
            submitted: false
        }
    },
    methods: {
        create: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                console.log(this.nacionalidad)
                axios.post('http://127.0.0.1:8000/api/propietario/',
                        this.propietario
                    )
                    .then(response => {
                        this.$router.push('/');
                    })
            });
        }
    },
}
</script>
