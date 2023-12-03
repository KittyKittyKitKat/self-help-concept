
const month_arr = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
const month_len = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
const days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

// current calendar data
let c_date = new Date();
let c_year = c_date.getFullYear();
let c_month = c_date.getMonth();
let c_startday = start_date(c_year, c_month);
let c_lastday = end_date(c_month);


function start_date(year, month) {
    let start_date = new Date(year, month, 1);
    return start_date.getDay();
}

function end_date(month) {
    return month_len[month]
}


/*
Generate a grid of buttons for each day.
*/
function generate_grid() {
    // check if grind-location exists

    let new_grid = document.createElement("div");
    new_grid.id = "grid-location";
    document.getElementById("grid-anchor").appendChild(new_grid);
    
    document.getElementById("month_entry").innerHTML = month_arr[c_month];
    document.getElementById("year_entry").innerHTML = c_year;
    let header = document.createElement("div");
    header.classList.add("row");
    for (let i = 0; i < 7; i++) {
        let header_col = document.createElement("div");
        header_col.classList.add("col", "grid-fix", "px-1");
        header_col.innerHTML = days[i];
        header.appendChild(header_col);
    }

    let count = 0;
    let id = 0;
    let dummy = false;

    new_grid.appendChild(header)
    for (let i = 0; i < 6; i++) { // need five rows to contain all possible days
        let new_row = document.createElement("div");
        new_row.classList.add("row", "entry");
        for (let j = 0; j < 7; j++) { 
            let new_col = document.createElement("div");
            new_col.classList.add("col", "grid-fix", "px-1");
            if (count >= start_date(c_year, c_month) && count < end_date(c_month) + start_date(c_year, c_month)) {
                dummy = false;
                id++;
            } else {
                dummy = true;
            }
            count++;
            btn = generate_day(new_col, id, dummy);
            new_col.appendChild(btn);
            new_row.appendChild(new_col);
        }
        
        new_grid.appendChild(new_row);
    }
}

function remove_grid() {
    document.getElementById("grid-location").remove();
}



function generate_day(col, id, dummy) {
    let btn = document.createElement("button");
    btn.classList.add("btn", "btn-dark", "my-1", "btn-day", "btn-circle");
    btn.innerHTML = id;
    btn.setAttribute("data-bs-target", "#staticBackdrop");
    btn.setAttribute("data-bs-toggle", "modal");
    btn.addEventListener("click", () => {
        update_day(id);
    });
    btn.id = id - 1;
    if (dummy) {
        btn.disabled = true
        btn.innerHTML = "";
    }
    return btn;
}

function update_day(id) {
    console.log(entry_arr[id]);
    document.getElementById("journal_entry").value = entry_arr[id];
}
    
function go_forward() {
    if (c_month == 11) {
        c_month = 0;
        c_year++;
    }
    else {
        c_month++;
    }

    remove_grid();
    generate_grid();
}

function go_back() {
    if (c_month == 0) {
        c_month = 11;
        c_year--;
    }
    else {
        c_month--;
    }

    remove_grid();
    generate_grid();
}
