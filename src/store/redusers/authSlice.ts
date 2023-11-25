import { createSlice } from "@reduxjs/toolkit";

const authSlice = createSlice({
    name: 'auth',
    initialState: {
        isAuth: false,
    },
    reducers: {
        setAuth(state) {
            state.isAuth = true
        },
        logout(state) {
            localStorage.removeItem('accessToken')
            localStorage.removeItem('role')
            state.isAuth = false
        }
    }
})

export const {setAuth, logout} = authSlice.actions

export default authSlice.reducer