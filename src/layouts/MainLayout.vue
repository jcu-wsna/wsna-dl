<template>
  <q-layout view="hHh lpr fFf" class="bg-accent">
    <q-header>
      <div class="q-pa-md bg-image">
        <q-toolbar class="bg-primary text-accent transparent">
          <q-toolbar-title>
            <h4 class="text-center">
              Water Security for Northern Australia Digital Library
            </h4>
          </q-toolbar-title>
        </q-toolbar>
        <q-toolbar class="bg-primary heavy">
          <q-tabs shrink>
            <q-route-tab to="/" label="About" />
            <q-route-tab to="/library" label="Library" />
            <q-route-tab to="/contact-us" label="Contact Us" />
          </q-tabs>
        </q-toolbar>
      </div>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer elevated>
      <q-toolbar>
        <q-toolbar-title>
          <div class="text-right text-subtitle1">
            Made with &hearts; by JCU eResearch
          </div>
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<style lang="scss">
.bg-image {
  background-image: url("/images/pexels-pixabay-355700.jpg");
  background-repeat: no-repeat;
  background-size: fit;
}

.heavy {
  opacity: 0.8;
}
</style>
