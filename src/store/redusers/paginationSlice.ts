import { createSlice } from "@reduxjs/toolkit";

const paginationSlice = createSlice({
    name: 'pagination',
    initialState: {
        isNext: false,
        next: '',
        prev: '',
    },
    reducers: {
        setNext(state) {
            state.isNext = true
        },
    }
})

export const {setNext} = paginationSlice.actions

export default paginationSlice.reducer