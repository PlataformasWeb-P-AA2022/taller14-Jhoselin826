<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <h2><router-link to="/index">Administración de Departamentos</router-link></h2>
        <router-link to="/create" class="btn btn-sm btn-primary">+ Propietario</router-link>
        <br>
        <router-link to="/departamento" class="btn btn-sm btn-primary">ver departamento</router-link>
        <br>
        <router-link to="/create_departamento" class="btn btn-sm btn-primary">+ departamentos</router-link>

        <router-view />
      </div>
    </div>
  </div>
</template>