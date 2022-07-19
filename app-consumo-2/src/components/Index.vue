<template>
    <div class="pt-5">
        <div v-if="estudiantes && estudiantes.length">
            <div class="card mb-3" v-for="estudiante of estudiantes" v-bind:key="estudiante.id">
                <div class="row no-gutters">
                    <div class="col-md-4">
                        <div class="card-body">
                            <h5 class="card-title">Nombre: {{ estudiante.nombre }}</h5>
                            <h5 class="card-text">Apellido: {{ estudiante.apellido }}</h5>
                            <br>
                            <router-link :to="{name: 'edit', params: { id: estudiante.id }}" class="btn btn-sm btn-primary">Editar</router-link>
                            <button class="btn btn-danger btn-sm ml-1" v-on:click="deleteEstudiante(estudiante)">Eliminar</button>
                        </div>
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <p class="card-text">Cédula: {{ estudiante.cedula }}</p>
                            <p class="card-text">Correo: {{ estudiante.correo }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <p  v-if="estudiantes.length == 0"> Sin Estudiantes</p>
    </div>
</template>
<script>

import axios from 'axios';

export default {
    data() {
        return {
            estudiantes: []
        }
    },
    created() {
        this.all();
    },
    methods: {
        deleteEstudiante: function(e) {
            if (confirm('Eliminar ' + e.nombre)) {
                axios.delete(e.url)
                    .then( response => {
                        this.all();
                    });
            }
        },
        all: function () {
            axios.get('http://127.0.0.1:8000/api/estudiantes/')
                .then( response => {
                    this.estudiantes = response.data
                });
        }
    },
}
</script>
