import Table from '../Component/Table'


const List = ({ company, location, level, tag }) => {

    return(
        <div className='list'>
            <Table company={company} location={location} level={level} tag={tag}/>
        </div>
    )
}

export default List