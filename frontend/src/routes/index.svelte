<script lang="ts">
    import Nav from "../components/nav.svelte"
    const a = 'test';
</script>
<svelte:head>
    <title>SWE Explore</title>
</svelte:head>
<h1>Software Engineer Explore</h1>
<p>{a}</p>
<Nav/>
<style>
    h1{
        color: crimson;
    }
</style>