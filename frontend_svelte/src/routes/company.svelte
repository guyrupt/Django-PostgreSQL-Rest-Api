<script>
    import { writable } from 'svelte/store';

    export const company = writable([]);

    const fetchData = async (company_name) => {
        const url = `http://127.0.0.1:8000/companystats/${company_name}`;
        const res = await fetch(url);
        const data = await res.json();
        company.set(data);
    };
    let searchTerm = "";
    let num = 0;
    $:{
        if(searchTerm.length>num){
            fetchData(searchTerm);
        }
        num = searchTerm.length;
    }
    console.log(company)
</script>
<svelte:head>
    <title>SWE Explore: Company</title>
</svelte:head>
<h1 class="text-4xl text-center my-8 uppercase">SWE Explore</h1>
<input class="w-full rounded-md text-lg p-4 border-2 border-gray-200" type="text" 
bind:value={searchTerm} placeholder="Search for Company Stats. Type in Company name.">

{#each $company as c}
<div class="flex p-6 space-x-4 bg-gray-100 text-gray-800 rounded-md shadow-sm text-center">
    <div class="flex-1">
        <img class="inline h-11 w-10 items-center" src={c.company.icon_url} alt={c.company.company_name}>
        <h2 class="inline uppercase text-lg items-center">{c.company.company_name}</h2>
    </div>
    <div class="flex-1 items-center my-auto">
        <p>Data Count</p> 
        <p>{c.count}</p>
    </div>
    <div class="flex-1 items-center my-auto">
        <p>Total Compensation Avg ($k/yr)</p>
        <p>{Math.round(c.totalyearlycompensation.totalyearlycompensation__avg)}</p>
    </div>
</div>
<div class="items-center font-black bg-gray-200 text-gray-800 shadow-sm text-center">
    Gender
</div>
<div class="flex p-6 text-center space-x-4 bg-gray-100 text-gray-800 rounded-md shadow-sm">
    <div class="flex-1 items-center my-auto">
        <p>N.A.</p>
        <p class="inline uppercase text-lg items-center">
            {c.gender.null}
        </p>
    </div>
    <div class="flex-1 items-center my-auto">
        <p>Male</p> 
        <p class="inline uppercase text-lg items-center">
            {c.gender.male}
        </p>
    </div>
    <div class="flex-1 items-center my-auto">
        <p>Female</p>
        <p class="inline uppercase text-lg items-center">
            {c.gender.female}
        </p>
    </div>
    <div class="flex-1 items-center my-auto">
        <p>Other</p>
        <p class="inline uppercase text-lg items-center">
            {c.gender.other}
        </p>
    </div>
</div>
<div class="items-center font-black bg-gray-200 text-gray-800 shadow-sm text-center">
    Race
</div>
<div class="flex p-6 space-x-4 bg-gray-100 text-gray-800 rounded-md shadow-sm text-center">
    <div class="flex-1 items-center my-auto">
        <p>N.A.</p>
        <p class="inline uppercase text-lg items-center">{c.race.null}</p>
    </div>
    <div class="flex-1 items-center my-auto">
        <p>White</p>
        <p class="inline uppercase text-lg items-center">
            {c.race.White}
        </p>
    </div>
    <div class="flex-1 items-center my-auto">
        <p>Asian</p>
        <p class="inline uppercase text-lg items-center">
            {c.race.Asian}
        </p>
    </div>
    <div class="flex-1 items-center my-auto">
        <p>Hispanic / Latino</p>
        <p class="inline uppercase text-lg items-center">{c.race.Hispanic_Latino}</p>
    </div>
    <div class="flex-1 items-center my-auto">
        <p>Two or More Races</p>
        <p class="inline uppercase text-lg items-center">{c.race.Two_or_More_Races}</p>
    </div>
    <div class="flex-1 items-center my-auto">
        <p>Black or African American</p>
        <p class="inline uppercase text-lg items-center">{c.race.Black_or_African_American}</p>
    </div>
    <div class="flex-1 items-center my-auto">
        <p>Native Hawaiian or Other Pacific Islander</p>
        <p class="inline uppercase text-lg items-center">
            {c.race.Native_Hawaiian_or_Other_Pacific_Islander}
        </p>
    </div>
    <div class="flex-1 items-center my-auto">
    <p>American Indian or Alaska Native</p>
        <p class="inline uppercase text-lg items-center">
            {c.race.American_Indian_or_Alaska_Native}
        </p>
    </div>
</div>
<div class="items-center font-black bg-gray-200 text-gray-800 shadow-sm text-center">
    Academic Level
</div>
<div class="flex p-6 text-center space-x-4 bg-gray-100 text-gray-800 rounded-md shadow-sm">
    <div class="flex-1 items-center my-auto">
        <p>N.A.</p>
        <p class="inline uppercase text-lg items-center">
            {c.academic_level.null}
        </p>
    </div>
    <div class="flex-1 items-center my-auto">
        <p>Bachelor</p> 
        <p class="inline uppercase text-lg items-center">
            {c.academic_level.Bachelor}
        </p>
    </div>
    <div class="flex-1 items-center my-auto">
        <p>Master</p>
        <p class="inline uppercase text-lg items-center">
            {c.academic_level.Master}
        </p>
    </div>
    <div class="flex-1 items-center my-auto">
        <p>Doctorate (PhD)</p>
        <p class="inline uppercase text-lg items-center">
            {c.academic_level.Doctorate_PhD}
        </p>
    </div>
    <div class="flex-1 items-center my-auto">
        <p>Some college coursework completed</p>
        <p class="inline uppercase text-lg items-center">
            {c.academic_level.Some_college_coursework_completed}
        </p>
    </div>
    <div class="flex-1 items-center my-auto">
        <p>High school or equivalent</p>
        <p class="inline uppercase text-lg items-center">
            {c.academic_level.High_school_or_equivalent}
        </p>
    </div>
    <div class="flex-1 items-center my-auto">
        <p>Technical or occupational certificate</p>
        <p class="inline uppercase text-lg items-center">
            {c.academic_level.Technical_or_occupational_certificate}
        </p>
    </div>
    <div class="flex-1 items-center my-auto">
        <p>Associate Degree</p>
        <p class="inline uppercase text-lg items-center">
            {c.academic_level.Associate_Degree}
        </p>
    </div>
</div>
<div class="items-center font-black bg-gray-200 text-gray-800 shadow-sm text-center">
    Levels and Total Compensation Avg ($k/yr)
</div>
    {#each c.levels as l}
        <div class="border-2 border-gray-300 flex p-6 text-left space-x-4 bg-gray-100 text-gray-800 rounded-md shadow-sm">
            <div class="flex-1 items-center my-auto">
                {l.level_name}
            </div>
            <div class="flex-1 items-center my-auto">
                {Math.round(l.avg_salary.totalyearlycompensation__avg)}
            </div>
        </div>
    {/each}

{/each}