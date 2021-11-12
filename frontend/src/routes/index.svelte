<script lang="ts">
    import EmployeeCard from "../components/employeeCard.svelte";
    import { writable } from 'svelte/store';

    export const employees = writable([]);

    const fetchData = async (location) => {
	    const url = `http://127.0.0.1:8000/location/${location}`;
	    const res = await fetch(url);
	    const data = await res.json();
    	employees.set(data);
    };
    let searchTerm = "";
    let l = 0;
    $:{
        if(searchTerm.length>l){
            fetchData(searchTerm);
        }
        l = searchTerm.length;
    }
</script>
<svelte:head>
    <title>SWE Explore</title>
</svelte:head>
<h1 class="text-4xl text-center my-8 uppercase">SWE Explore</h1>
<input class="w-full rounded-md text-lg p-4 border-2 border-gray-200" type="text" 
bind:value={searchTerm} placeholder="Search location. Use either country or U.S. states abbreviation">
<table class="table-auto w-full p-4 border-2 bg-blue-300 text-gray-800 shadow-sm text-left rounded-md">
    <thead>
      <tr>
        <th class="w-1/5">Company</th>
        <th class="w-1/5">Level Name</th>
        <th class="w-1/5">Years of Experience</th>
        <th class="w-1/5">Academic Level</th>
        <th class="w-1/5">Total Compensation ($/yr)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Location</td>
        <td>Tag</td>
        <td>At Company | Total</td>
        <td>Gender | Race</td>
        <td>Base | Stock | Bonus</td>
      </tr>
      
    </tbody>
  </table>
<div class="py-4 grid gap-4 grid-cols-1">
{#each $employees as employee}
<EmployeeCard employee = {employee}/>
{/each}
</div>

<style>
    
</style>