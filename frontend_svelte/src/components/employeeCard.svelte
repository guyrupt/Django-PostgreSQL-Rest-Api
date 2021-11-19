<script>
    import { name } from '../stores';
    export let employee;
    function handleClick(){
      name.set(employee.company.company);
    }
</script>
<!-- <a class="p-6 bg-gray-100 text-gray-800 text-center rounded-md 
shadow-sm hover:shadow-md flex flex-col items-center"href={`/employee/${employee.id}`}>
    <img class="h-10 w-10" src={employee.company.icon_url} alt={employee.company.company}>
    <h2 class="uppercase text-lg">{employee.company.company}</h2>
</a> -->

<a class="hover:shadow-md w-full" on:click={handleClick} href={'/company'}>
  <table class="table-auto p-6 bg-gray-100 text-gray-800 rounded-md shadow-sm text-left w-full">
    <thead>
      <tr>
        <th class="w-1/5"><img class="h-10 w-10" src={employee.company.icon_url} alt={employee.company.company}></th>
        <th class="w-1/5">{employee.level}</th>
        <th class="w-1/5 my-auto">{employee.yearsatcompany} | {employee.yearsofexperience}</th>
        <th class="w-1/5">{employee.academic_level}</th>
        <th class="w-1/5">{employee.totalyearlycompensation}</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>{employee.company.company}<p>{employee.location}</p></td>
        <td>{employee.tag}</td>
        <td></td>
        <td>{employee.gender} | {employee.race}</td>
        <td>{employee.base_salary} | {employee.stockgrantvalue} | {employee.bonus}</td>
      </tr>
    </tbody>
  </table>
</a>