<template>
    <div class="pt-5">
        <form @submit.prevent="create" method="post">
            <div class="form-group">
                <label for="costo">Costo del departamento</label>
                <input
                    type="text"
                    class="form-control"
                    id="costo"
                    v-model="departamento.costo"
                    v-validate="'required'"
                    name="costo"
                    placeholder="Ingrese costo"
                    :class="{'is-invalid': errors.has('departamento.costo') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid costo.
                </div>
            </div>

            <div class="form-group">
                <label for="nroCuartos">Numero de cuartos</label>
                <input
                    type="text"
                    class="form-control"
                    id="nroCuartos"
                    v-model="departamento.nroCuartos"
                    v-validate="'required'"
                    name="nroCuartos"
                    placeholder="Ingrese Numero de cuartos"
                    :class="{'is-invalid': errors.has('departamento.nroCuartos') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid nroCuartos.
                </div>
            </div>

            <div class="form-group">
                <label for="numeroBanioos">Numero de baños</label>
                <input
                    type="text"
                    class="form-control"
                    id="numeroBanios"
                    v-model="departamento.numeroBanios"
                    v-validate="'required'"
                    name="numeroBanios"
                    placeholder="Ingrese Numero de baños"
                    :class="{'is-invalid': errors.has('departamento.numeroBanios') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid numeroBanios.
                </div>
            </div>

            <div class="form-group">
                <label for="valorAlicuota">Valor de alicuota</label>
                <input
                    type="text"
                    class="form-control"
                    id="valorAlicuota"
                    v-model="departamento.valorAlicuota"
                    v-validate="'required'"
                    name="valorAlicuota"
                    placeholder="Ingrese Valor de alicuota"
                    :class="{'is-invalid': errors.has('departamento.valorAlicuota') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid valorAlicuota.
                </div>
            </div>

            <div class="form-group">
              <br>
                <label for="propietario">Propietario</label>
                <select v-model="departamento.propietario">
                            <option v-for="e in propietariosList" :key="e.url" :value="e.url">{{ e.nombre }} {{ e.apellido }}</option>
                        </select>
            </div>
            <br>
            <button type="submit" class="btn btn-primary">Crear</button>
        </form>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    data() {
        return {
            departamento: {
                costo: '',
                nroCuartos: '',
                nroBaños: '',
                valorAlicuota: '',
                propietario: '',
            },
            propietariosList: [],
            submitted: false
        }
    },
    mounted() {
        this.getPropietariosList()
    },
    methods: {
      getEstudiantesList() {
            axios
            .get('http://127.0.0.1:8000/api/propietarios/')
            .then(response => {
                this.propietariosList = response.data
            })
            .catch(error => {
                console.log(error)
            })

        },
        create: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                axios.post('http://127.0.0.1:8000/api/departamentos/',
                        this.departamento
                    )
                    .then(response => {
                        this.$router.push('/departamentos');
                    })
            });
        }
    },
}
</script>