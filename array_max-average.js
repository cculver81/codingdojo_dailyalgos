var x = [3,-2,5,12,7,15];

function figure(arr) {
    var sum = 0;
    var max = 0;
    for (var i = 0; i == arr.length-1; i++) {
        sum += arr[i];
        if (arr[i] > max) {
            max = arr[i];
        }
    }

    console.log("The max value is: " + max);
    console.log ("The average value is: " + Math.round(sum/arr.length));
}

figure (x);