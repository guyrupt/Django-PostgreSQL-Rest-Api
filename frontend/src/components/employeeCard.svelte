<script>
    export let employee;
</script>
<!-- <a class="p-6 bg-gray-100 text-gray-800 text-center rounded-md 
shadow-sm hover:shadow-md flex flex-col items-center"href={`/employee/${employee.id}`}>
    <img class="h-10 w-10" src={employee.company.icon_url} alt={employee.company.company}>
    <h2 class="uppercase text-lg">{employee.company.company}</h2>
</a> -->

<table class="table-auto p-6 bg-gray-100 text-gray-800 rounded-md shadow-sm text-left">
    <thead>
      <tr>
        <th class="w-1/5"><img class="h-10 w-10" src={employee.company.icon_url} alt={employee.company.company}></th>
        <th class="w-1/5">{employee.level}</th>
        <th class="w-1/5">{employee.yearsatcompany} | {employee.yearsofexperience}</th>
        <th class="w-1/5">{employee.academic_level}</th>
        <th class="w-1/5">{employee.totalyearlycompensation}</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>{employee.company.company} | {employee.location}</td>
        <td>{employee.tag}</td>
        <td></td>
        <td>{employee.gender} | {employee.race}</td>
        <td>{employee.base_salary} | {employee.stockgrantvalue} | {employee.bonus}</td>
      </tr>
    </tbody>
  </table>
