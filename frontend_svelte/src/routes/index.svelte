<script lang="ts">
    import EmployeeCard from "../components/employeeCard.svelte";
    import { writable } from 'svelte/store';

    export const employees = writable([]);

    const fetchData = async (location) => {
	    const url = `http://127.0.0.1:8000/location/${location}`;
	    const res = await fetch(url);
	    const data = await res.json();
    	employees.set(data);
      return 1;
    };
    let searchTerm = "";
    let promise;
    let temp = '';
    const onKeyPress = e => {
        if (e.charCode === 13) searchTerm = temp;
    };
    $:{
        if(searchTerm.length>0){
            promise = fetchData(searchTerm);
        }
    }
</script>
<svelte:head>
    <title>SWE Explore: Location</title>
</svelte:head>
<h1 class="text-4xl text-center my-8 uppercase">SWE Explore</h1>
<input class="w-full rounded-md text-lg p-4 border-2 border-gray-200" type="text" on:keypress={onKeyPress} 
bind:value={temp} placeholder="Search location. Use either country or U.S. states abbreviation.">
<table class="table-auto w-full border-2 bg-blue-300 text-gray-800 shadow-sm text-left rounded-md items-center">
    <thead>
      <tr>
        <th class="w-1/5">Company</th>
        <th class="w-1/5">Level Name</th>
        <th class="w-1/5">Years of Experience</th>
        <th class="w-1/5">Academic Level</th>
        <th class="w-1/5">Total Compensation ($k/yr)</th>
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
{#await promise}
  <p>...waiting</p>
{/await}
{#each $employees as employee}
<EmployeeCard employee = {employee}/>
{/each}
</div>

<style>
    
</style>