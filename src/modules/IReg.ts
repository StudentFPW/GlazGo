import { IUser } from "./IUser"

export interface IRegQueryData extends IUser {
    password: string
}
export interface IRegResponseData {
    access: string
    refresh: string
    user: IUser
}
