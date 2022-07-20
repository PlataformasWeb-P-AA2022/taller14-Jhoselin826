<template>
    <div class="pt-5">
        <form @submit.prevent="update" method="post">
            <div class="form-group">
                <label for="nombre">Nombre</label>
                <input
                    type="text"
                    class="form-control"
                    id="nombre"
                    v-model="propietario.nombre"
                    v-validate="'required'"
                    name="nombre"
                    placeholder="Ingrese nombre"
                    :class="{'is-invalid': errors.has('propietario.nombre') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid name.
                </div>
            </div>
            <div class="form-group">
                <label for="apellido">Apellido</label>
                <textarea
                    name="apellido"
                    class="form-control"
                    id="apellido"
                    v-validate="'required'"
                    v-model="propietario.apellido"
                    cols="30"
                    rows="2"
                    :class="{'is-invalid': errors.has('propietario.apellido') && submitted}">
                  </textarea>
                <div class="invalid-feedback">
                    Please provide a valid description.
                </div>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
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
                url: '',
            },
            submitted: false
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/api/propietario/' + this.$route.params.id + '/')
            .then( response => {
                console.log(response.data)
                this.propietario = response.data
            });
    },
    methods: {
        update: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                axios.put(`http://127.0.0.1:8000/api/propietario/${this.propietario.id}/`,
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
