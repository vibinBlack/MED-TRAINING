export class doctor{
    id!:number;
    first_name!:string;
    last_name!:string;
    type!:string;
}

export class appointment{
    id!:number;
    doctor!:string;
    type!:string;
    date!:Date;
    time!:string;
    patient!:string;
}

export class patient{
    name!:string;
    email!:string;
    mobile_number!:string;
    location!:string;
}