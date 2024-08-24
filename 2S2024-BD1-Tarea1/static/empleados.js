document.addEventListener('DOMContentLoaded', async () => {
    try {
        const response = await fetch('/listar_empleados');

        if (!response.ok) {
            throw new Error('Error al obtener la lista de empleados');
        }

        const empleados = await response.json();
        console.log('Empleados:', empleados); // Agrega esta línea para ver la respuesta

        // Obtén el cuerpo de la tabla donde se agregarán los empleados
        const employeeTableBody = document.getElementById('employeeTableBody');

        // Limpia cualquier fila existente en la tabla
        employeeTableBody.innerHTML = '';

        // Recorre la lista de empleados y crea una fila para cada uno
        empleados.forEach(empleado => {
            const row = document.createElement('tr');

            const idCell = document.createElement('td');

            idCell.textContent = empleado.Id;
            
            row.appendChild(idCell);
            

            const nombreCell = document.createElement('td');
            nombreCell.textContent = empleado.Nombre;
            row.appendChild(nombreCell);

            const salarioCell = document.createElement('td');
            salarioCell.textContent = empleado.Salario;
            row.appendChild(salarioCell);

            // Agrega la fila a la tabla
            employeeTableBody.appendChild(row);
        });
        
    } catch (error) {
        console.error('Error al cargar empleados:', error);
        alert('Ocurrió un error al cargar la lista de empleados. Por favor, inténtelo de nuevo más tarde.');
    }
});
