<template>
    <div class="pt-5">
        <div v-if="telefonos && telefonos.length">
            <div class="card mb-3" v-for="telefono of telefonos" v-bind:key="telefono.id">
                <div class="row no-gutters">
                    <div class="col-md-4">
                        <div class="card-body">
                            <span class="card-title"><b>Número:</b> {{ telefono.telefono }}</span>
                            <br>
                            <span class="card-text"><b>Tipo:</b> {{ telefono.tipo }}</span>
                            <br>
                            <router-link :to="{name: 'edit_telefono', params: { id: telefono.id }}" class="btn btn-sm btn-primary">Editar</router-link>
                            <button class="btn btn-danger btn-sm ml-1" v-on:click="deleteTelefono(telefono)">Eliminar</button>
                        </div>
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <span class="card-text"><b>Estudiante:</b> {{ telefono.estudiante_str }}</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <p  v-if="telefonos.length == 0"> Sin Telefonos</p>
    </div>
</template>
<script>

import axios from 'axios';

export default {
    data() {
        return {
            telefonos: []
        }
    },
    created() {
        this.all();
    },
    methods: {
        deleteTelefono: function(e) {
            if (confirm('Eliminar ' + e.telefono)) {
                axios.delete(e.url)
                    .then( response => {
                        this.all();
                    });
            }
        },
        all: function () {
            axios.get('http://127.0.0.1:8000/api/numerost/')
                .then( response => {
                    this.telefonos = response.data
                });
        }
    },
}
</script>
